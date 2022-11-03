#Declaring Global Variables
ShutDownRequest=False
ConExists=False
def StartDatabaseProcess(ConnectionObject):
    global ShutDownRequest
    from Codebase.ErrorLogs.logging import Log,DBLog,ErrorLog
    from multiprocessing import process
    DataBaseProcess=process()
    DataBaseProcess.start()
    from time import sleep
    Log(f"ProcessStarted {ShutDownRequest} is the request now")
    while ShutDownRequest==False:
        sleep(2)
    else:    
        DBLog("Shutdown Requested")
        TryCount=5
        while TryCount:
            try:
                ConnectionObject.commit()
                ConnectionObject.close()
                break
            except:
                TryCount-=1
                ErrorLog("Connection Failed to Close")
                DBLog("Connection Failed to Close")
        Log("Loop Terminated")
    print("ProcessDone")


def SignalShutDown():
    global ShutDownRequest
    ShutDownRequest=True






