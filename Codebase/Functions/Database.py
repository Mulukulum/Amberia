import sqlite3                                      
from Codebase.Variables import DataBasePath         #Get the location of the Database
ConnectionObject=sqlite3.connect(DataBasePath)      #Creates the connection to the databse
def ExecuteCommand(cmd,iterable=None):              #Takes a cmd string and an optional iterable to replace a placeholder
    global ConnectionObject
    cursor=ConnectionObject.cursor()                #Creates cursor object
    if iterable==None:
        result=cursor.execute(cmd)
    else:
        result=cursor.execute(cmd,iterable)
    result=result.fetchall()                        #Fetches results
    ConnectionObject.commit()                       #Commits the database
    return result                                   #Returns the list
    
def ExecuteManyCommands(cmd,iterable=None):         #Takes a cmd string and an optional iterable for placeholders
    global ConnectionObject                             
    cursor=ConnectionObject.cursor()                #Creates cursor object
    if iterable==None:
        result=cursor.executemany(cmd)
    else:
        result=cursor.executemany(cmd,iterable)
    result=result.fetchall()                        #Fetches results
    ConnectionObject.commit()                       #Commits the database
    return result                                   #Returns the list

def ExecuteScript(cmd):
    global ConnectionObject
    cursor=ConnectionObject.cursor()                #Creates cursor
    result=cursor.executescript(cmd)                #Executes the script
    result=result.fetchall()                        #Returns the list
    ConnectionObject.commit()                       #Commits changes
    return result                                   #Returns the list

def CloseConnection():
    global ConnectionObject     
    ConnectionObject.close()                        #Closes the connection
    ConnectionObject=None                           #Sets the conn


