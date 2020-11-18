# python_sqlplus

The utility run_all_sql_dir.py executes all sql files from the specified directory and creates one log files.
in the script you can configure NLS variables:

    NLS_DATE_FORMAT = "\'DD.MM.YYYY HH24:MI:SS\'"
    NLS_NUMERIC_CHARACTERS = "\'.,\'"
    NLS_LANG = 'AMERICAN_AMERICA.CL8MSWIN1251'

, autocommit,

    AUTO_COMMIT = "OFF"

stop the script on error or continue execution

    WHENEVER = 'WHENEVER SQLERROR EXIT SQL.SQLCODE'.


-u Specify the username for example SCOTT

-p Specify the password for example TIGER

-c Specify the connect_string(TNS alias) or easy connect string for connect to oracle database

-d Specify the directory for executing sql scripts.

-l Specify the logfile for output log.

for example

    run_all_sql_dir.py -u scott -p tiger -c 192.168.0.166:1521/test -d C:\Users\Dmitry\PycharmProjects\count_char\sql  -l log_sql.log