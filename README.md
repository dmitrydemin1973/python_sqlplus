# python_sqlplus

The utility run_all_sql_dir.py executes all sql files from the specified directory and creates one log files.
The utility can also generate a summary SQL file with calls to sql files without executing sql on the oracle server.

In the script you can configure NLS variables:

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

-s Specify the SQL file for summary output.

for example, the utility connects to the database with parameters username, password, connect string and executes all sql files in directory.

    run_all_sql_dir.py -u scott -p tiger -c 192.168.0.166:1521/test -d C:\Users\Dmitry\PycharmProjects\count_char\sql  -l log_sql.log

for example, the utility does not connect to the database and makes a summary sql script.

    run_all_sql_dir.py -d C:\Users\Dmitry\PycharmProjects\count_char\sql  -s summary_sql_script.sql  -l log_sql.log