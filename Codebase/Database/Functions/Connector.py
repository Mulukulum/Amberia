ShutDownRequest=False #Flag used to signal when to stop
Connection=-1
DataBasePath=None
ConExists=False
from Codebase.ErrorLogs.logging import ErrorLog,DBLog,Log
def EntryPoint(DataPath):
    global Connection,DataBasePath
    DataBasePath=DataPath
    Connection=_ActivateDatabase()
    print(f"global con is {Connection}")
    return Connection

def RunDatabaseThread():
    global Connection,ShutDownRequest
    from time import sleep
    sleep(0.1)
    Log("ProcessStarted")
    Log(f"{ShutDownRequest} is the request now")
    while ShutDownRequest==False:
        Log("Nap")
        sleep(2)
        Log("Wakey")
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

    