import sqlite3
from Codebase.Database import DataBasePath      #Gets the path of the database on the machine
from Codebase.Database.Functions.StartUp import CheckAndCreate
Con=sqlite3.connect(DataBasePath)       #Creates the database file if it doesn't exist already and makes a connection
Cursor=Con.cursor()

'''
LIST OF TABLES

The following is a list of all tables that should be present in the Database

projects
Attributes :-
ID Text PRIMARY KEY
ParentID Text


labels
Attributes:-


tasks
Attributes:-


sections
Attributes:-





'''
#Check if the Following Tables exist
CheckList=('projects',
            'labels',
            'tasks',
            'sections')

AttribDict={'projects':'(ID TEXT PRIMARY KEY,TITLE TEXT,COLOR )',
            'labels':2,
            'tasks':2,
            'sections':2}

#









Con.commit()
Con.close()