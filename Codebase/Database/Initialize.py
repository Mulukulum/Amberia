from os.path import dirname                     
import sqlite3  
from Codebase.Database.StartUp import CheckAndCreate        
from Codebase.ErrorLogs.logging import StartLog,ErrorLog
StartLog("Initialisation Requested")

DataBasePath=dirname(__file__)+r"\Data\Amber.db"

Con=sqlite3.connect(DataBasePath)       #Creates the database file if it doesn't exist already and makes a connection
Cursor=Con.cursor()                     #Creates a cursor object from the connection that we can do operations with

#Check if the Following Tables exist
#   DO NOT FORGET TO MODIFY THE READTHIS.MD FILE
#   DO NOT FORGET TO MODIFY THE READTHIS.MD FILE
#   DO NOT FORGET TO MODIFY THE READTHIS.MD FILE
CheckList=('projects',
            'labels',
            'tasks',
            'sections',
            'prcolors')
#   MODIFY README.MD WHEN MAKING ANY CHANGES TO ANY OF THIS
#   MODIFY README.MD WHEN MAKING ANY CHANGES TO ANY OF THIS
#   MODIFY README.MD WHEN MAKING ANY CHANGES TO ANY OF THIS
AttribDict={
    'projects':'id INTEGER PRIMARY KEY, parentid INTEGER, title TEXT NOT NULL, color TEXT NOT NULL, sectioncount INTEGER NOT NULL, projectcount INTEGER NOT NULL, projecttemplate INTEGER',
    'labels':'title TEXT PRIMARY KEY, color TEXT NOT NULL,taskcount INTEGER NOT NULL',
    'tasks':'taskid INTEGER PRIMARY KEY, title TEXT NOT NULL, parentid INTEGER NOT NULL, sectionid INTEGER, priority INTEGER NOT NULL, color INTEGER NOT NULL, tasktemplate INTEGER',
    'sections':'sectionid INTEGER PRIMARY KEY, title TEXT NOT NULL, taskcount INTEGER NOT NULL, parentprojectid INTEGER NOT NULL, sectiontemplate INTEGER',
    'prcolors':'level INTEGER PRIMARY KEY, clrvalue INTEGER NOT NULL',
    }
#   DO NOT FORGET TO MODIFY THE READTHIS.MD FILE
#   DO NOT FORGET TO MODIFY THE READTHIS.MD FILE
#   DO NOT FORGET TO MODIFY THE READTHIS.MD FILE
CriticalError=False
for table in CheckList:                                 #For the tables that have to be checked
    if CheckAndCreate(Cursor,table,AttribDict[table]):  #iterate through each one and ensure the tables exist
        StartLog(f"TABLE {table} exists now with Attributes {AttribDict[table]}")         #If they exist, Log it into a file
    else:
        ErrorLog(f"Could not create TABLE {table} with Attributes {AttribDict[table]}")   #If they don't exist, log which one doesn't exist and shut the whole thing down
        CriticalError=True
Con.commit()                #Commits Changes
Con.close()                 #Closes Connection
if CriticalError:
    ErrorLog("CRITICAL: Database could not be initialised. Check Start Logs for more information")
StartLog("Initialisation of Database Completed")
#Now that all tables have been created, database can have values put into it.
#Initialization of Database is done at this point.