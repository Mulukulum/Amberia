ShutDownRequest=False #Flag used to signal when to stop
Connection=-1
from Codebase.ErrorLogs.logging import ErrorLog,DBLog
def EntryPoint():
    from threading import Thread
    try:
        thread=Thread(target=RunDatabaseThread)
        thread.start()
        return thread
    except:
        ErrorLog("Could Not Activate Database")
def RunDatabaseThread():
    global Connection,ShutDownRequest
    Connection=_ActivateDatabase()
    from time import sleep
    while ShutDownRequest==False:
        print('Sleeping...')
    else:    
        DBLog("Shutdown Requested")
        print("ShutDown")
        TryCount=5
        while TryCount:
            try:
                Connection.commit()
                Connection.close()
                break
            except:
                TryCount-=1
                ErrorLog("Connection Failed to Close")
                DBLog("Connection Failed to Close")

def GetConnection():
    global Connection
    return Connection

def _ActivateDatabase():
    from Codebase.Database import DataBasePath
    import sqlite3
    from Codebase.ErrorLogs.logging import ErrorLog,DBOnlyLog,DBLog,StartLog
    StartLog("Database Activation Requested")
    try:
        con=sqlite3.connect(DataBasePath)
        DBOnlyLog("Database Activated For Usage")
        return con
    except:
        DBLog("Database Activation Failure")
        ErrorLog("Database Activation Failure")

def SignalShutDown():
    global ShutDownRequest
    ShutDownRequest=True

    