ShutDownRequest=False #Flag used to signal when to stop
Connection=-1
from Codebase.ErrorLogs.logging import ErrorLog,DBLog,Log
def EntryPoint():
    from threading import Thread
    try:
        thread=Thread(target=RunDatabaseThread,daemon=False)
        thread.start()
        return thread
    except:
        ErrorLog("Could Not Activate Database")
def RunDatabaseThread():
    global Connection,ShutDownRequest
    import sys
    Connection=_ActivateDatabase()
    ErrorLog("ThreadStarted")
    from time import sleep
    print(f"{ShutDownRequest} is the request now",file=sys.stdout,flush=True)
    while ShutDownRequest==False:
        Log('Sleeping...')
        sleep(0.5)
        Log('Slept')
    else:    
        DBLog("Shutdown Requested")
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
        Log("Loop Terminated")
    print("ThreadDone")
    

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
    print(ShutDownRequest)
    ShutDownRequest=True
    print(ShutDownRequest)

    