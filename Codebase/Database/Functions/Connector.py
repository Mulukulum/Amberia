ShutDownRequest=False #Flag used to signal when to stop
def EntryPoint():
    print("Entry Request")
    ShutDownRequest=False #Flag used to signal when to stop
    Connection=ActivateDatabase()
    def GetCursor():
        global Connection
        return Connection.cursor()

def ActivateDatabase():
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

def _CheckShutDown():
    from time import sleep
    while ShutDownRequest==False:
        sleep(5) ; print('Sleeping...')

    