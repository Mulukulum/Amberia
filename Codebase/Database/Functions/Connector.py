ShutDownRequest=False #Flag used to signal when to stop
Connection=-1
DataBasePath=None
ConExists=False
from Codebase.ErrorLogs.logging import ErrorLog,DBLog,Log
def EntryPoint(DataPath):
    global Connection,DataBasePath
    DataBasePath=DataPath
    Connection=_ActivateDatabase()
    from multiprocessing import Process as Proc
    print(f"global con is {Connection}")
    try:
        print("Connection is Good to Go")
        Process=Proc(target=RunDatabaseThread)
        Process.start()
        return Process
    except:
        ErrorLog("Could Not Activate Database")
def RunDatabaseThread():
    global Connection,ShutDownRequest
    Log("ThreadStarted")
    from time import sleep
    print(f"{ShutDownRequest} is the request now")
    while ShutDownRequest==False:
        sleep(1)
    else:    
        print("ShutDown Wanted")
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
    print("ProcessDone")

def GetCursor():
    global Connection
    print(f"Connection Is {Connection}")
    return Connection.cursor()

def _ActivateDatabase():
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

    