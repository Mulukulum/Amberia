This folder is for log files for various things.
The code that runs this is located at:
[Logging.py](../Codebase/ErrorLogs/logging.py)

Ctrl+Click to follow link

Use:
Log to log normal things
ErrorLogs to Log Errors
DBLog to log important things related to the database
DBOnlyLog writes only to the database log 

Use DBOnlyLog to ensure that Master.log isn't cluttered 
Reserve using DBLog for big important things

Don't use StartLog For anything