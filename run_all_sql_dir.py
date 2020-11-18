import os
import subprocess
import pathlib
from optparse import OptionParser
import logging

NLS_DATE_FORMAT = "\'DD.MM.YYYY HH24:MI:SS\'"
NLS_NUMERIC_CHARACTERS = "\'.,\'"
AUTO_COMMIT = "OFF"
NLS_LANG = 'AMERICAN_AMERICA.CL8MSWIN1251'
WHENEVER = 'WHENEVER SQLERROR EXIT SQL.SQLCODE'
#WHENEVER = 'WHENEVER SQLERROR CONTINUE'
# silent sqlplus = "-s"  silent off sqlplus = ""
silent_sqlplus = ""

Sqlheader = WHENEVER + """\n
set autocommit """ + AUTO_COMMIT + "\n" + \
"""set define off 
set timing on
set linesize 10000
set pagesize 10000
set pause off
set echo on
set heading on
set termout ON
SET FEEDBACK ON
SET TAB ON
SET UNDERLINE ON
set trimspool on
""" + "ALTER SESSION SET NLS_NUMERIC_CHARACTERS = " + NLS_NUMERIC_CHARACTERS + ";" + """
ALTER SESSION SET NLS_DATE_FORMAT = """ + NLS_DATE_FORMAT + ";\n"

parser = OptionParser(usage="usage: %%prog\n%s" % __doc__)
parser.add_option("-u", "--username", dest="username",
                  default=None,
                  help="User name of DB Oracle ")

parser.add_option("-p", "--password", dest="password",
                  default=None,
                  help="User Password of DB Oracle ")

parser.add_option("-c", "--connectstring", dest="connectstring",
                  default=None,
                  help="Connect string for DB Oracle ")

parser.add_option("-d", "--dir", dest="dirname",
                  default=None,
                  help="Name of dir sql ")

parser.add_option("-l", "--log", dest="logfilename",
                  default=None,
                  help="Name of log file ")

(options, args) = parser.parse_args()
input_dir_sql = options.dirname
username = options.username
password = options.password
connectstring = options.connectstring
logfilename = options.logfilename

logging.basicConfig(format='%(asctime)s %(levelname)s  %(message)s', filename=logfilename, level=logging.DEBUG)

logging.info('Start  script ')

sqlscript = ""
connectoracle = ''

currentDirectory = pathlib.Path(input_dir_sql)
for currentFile in currentDirectory.iterdir():
    sqlscript = sqlscript + "PROMPT Start script: " + currentFile.__str__() + "\n"
    sqlscript = sqlscript + "@" + currentFile.__str__() + "\n"
    sqlscript = sqlscript + "PROMPT Stop script: " + currentFile.__str__() + "\n"
    sqlscript = sqlscript + "PROMPT -------------------------------------------------------------------------------------- \n\n"
    logging.info('Found  script:' + currentFile.__str__())

SqlQueryALL = Sqlheader + sqlscript
logging.debug("Sqlfile:\n" + SqlQueryALL)

my_env = os.environ.copy()
my_env["NLS_LANG"] = NLS_LANG
logging.info("Set AUTO_COMMIT="+AUTO_COMMIT)
logging.info("Set NLS_LANG=" + NLS_LANG)
logging.info("Set NLS_DATE_FORMAT=" + NLS_DATE_FORMAT )
logging.info("Set NLS_NUMERIC_CHARACTERS=" + NLS_NUMERIC_CHARACTERS)
logging.info('Set ' + WHENEVER)

connectoracle = str(username) + "/" + str(password) + '@' + str(connectstring)

logging.info("Connect ro oracle:" + connectoracle)
sqlplus_result = subprocess.run([r'sqlplus.exe', silent_sqlplus, connectoracle], env=my_env,
                                stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, input=SqlQueryALL)


logging.info(sqlplus_result.stdout)

if sqlplus_result.returncode > 0:
    ORACLE_ERROR = "Oracle error ORA-" + str(sqlplus_result.returncode)
    print(ORACLE_ERROR)
    logging.error(ORACLE_ERROR)

logging.info('Stop  script')
