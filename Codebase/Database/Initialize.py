from os.path import dirname
import sqlite3
from Codebase.Database.Functions.StartUp import CheckAndCreate
from Codebase.ErrorLogs.logging import StartLog,ErrorLog
StartLog("Initialisation Requested")

DataBasePath=dirname(__file__)+r"\Data\Amber.db"

Con=sqlite3.connect(DataBasePath)       #Creates the database file if it doesn't exist already and makes a connection
Cursor=Con.cursor()                     #Creates a cursor object from the connection that we can do operations with

'''
LIST OF TABLES

The following is a list of all tables and their attributes that should be present in the Database

projects
Attributes :-
id INTEGER PRIMARY KEY
parentid INTEGER
title TEXT NOT NULL
color TEXT NOT NULL
sectioncount INTEGER NOT NULL
projectcount INTEGER NOT NULL
projecttemplate INTEGER

labels 
There is no ID here because having Labels with the same titles is a bad idea
Attributes:-
title TEXT PRIMARY KEY
color TEXT NOT NULL
taskcount INTEGER NOT NULL                          

tasks
(parentid is same as sectionid for a regular task, sectionid can be null for a subtask)
Attributes:-
taskid INTEGER PRIMARY KEY
title TEXT NOT NULL
parentid INTEGER NOT NULL 
sectionid INTEGER
priority INTEGER NOT NULL
color INTEGER NOT NULL
tasktemplate INTEGER

sections
Attributes:-
sectionid INTEGER PRIMARY KEY
title TEXT NOT NULL
taskcount INTEGER NOT NULL
parentprojectid INTEGER NOT NULL
sectiontemplate INTEGER

prcolors
Attributes:-
level INTEGER PRIMARY KEY
hexcode TEXT NOT NULL

'''
#Check if the Following Tables exist
CheckList=('projects',
            'labels',
            'tasks',
            'sections',
            'prcolors')

AttribDict={
    'projects':'id INTEGER PRIMARY KEY, parentid INTEGER, title TEXT NOT NULL, color TEXT NOT NULL, sectioncount INTEGER NOT NULL, projectcount INTEGER NOT NULL, projecttemplate INTEGER',
    'labels':'title TEXT PRIMARY KEY, color TEXT NOT NULL,taskcount INTEGER NOT NULL',
    'tasks':'taskid INTEGER PRIMARY KEY, title TEXT NOT NULL, parentid INTEGER NOT NULL, sectionid INTEGER, priority INTEGER NOT NULL, color INTEGER NOT NULL, tasktemplate INTEGER',
    'sections':'sectionid INTEGER PRIMARY KEY, title TEXT NOT NULL, taskcount INTEGER NOT NULL, parentprojectid INTEGER NOT NULL, sectiontemplate INTEGER',
    'prcolors':'level INTEGER PRIMARY KEY, hexcode TEXT NOT NULL',
    }
CriticalError=False
for table in CheckList:                                 #For the tables that have to be checked
    if CheckAndCreate(Cursor,table,AttribDict[table]):  #iterate through each one and ensure the tables exist
        StartLog(f"TABLE {table} exists with Attributes {AttribDict[table]}")         #If they exist, Log it into a file
    else:
        ErrorLog(f"Could not create TABLE {table} with Attributes {AttribDict[table]}")   #If they don't exist, log which one doesn't exist and shut the whole thing down
        CriticalError=True
Con.commit()
Con.close()
if CriticalError:
    ErrorLog("CRITICAL: Database could not be initialised. Check Start Logs for more information")
from threading import Thread
from Codebase.Database.Functions.Connector import EntryPoint
try:
    thread=Thread(target=EntryPoint)
    thread.start()
except:
    ErrorLog("Could Not Activate Database")

#Now that all tables have been created, database can have values put into it.
#Initialization of Database is done at this point.