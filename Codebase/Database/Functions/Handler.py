from Codebase.ErrorLogs.logging import ErrorLog,DBLog
import sqlite3

RefreshCycle=False
AssignedDuringRCycle=False
ServingID=0
LatestID=1
ResultDict=dict()
ReadyList=list()


def IDGenerator():
    global RefreshCycle,AssignedDuringRCycle,LatestID
    if RefreshCycle:
        if AssignedDuringRCycle:
            return LatestID+1
        else: 
            AssignedDuringRCycle=True
            return 1
    else:
        return LatestID+1

def NoReturnSingleExecutor(con,cmd):
    try:
        con.execute(cmd)
    except:
        ErrorLog(f"ERROR WHILE PROCESSING {cmd}")
        DBLog(f"ERROR WHILE PROCESSING {cmd}")
    con.commit()

def SingleExecutor(con,cmd):
    try:
        res=con.execute(cmd)    
    except:
        ErrorLog(f"ERROR WHILE PROCESSING {cmd}")
        DBLog(f"ERROR WHILE PROCESSING {cmd}")
        return -1
    ret=res.fetchall()
    con.commit()
    return ret

def StartRCycle():
    global RefreshCycle,LatestID
    RefreshCycle=True
    LatestID=1



    