import sqlite3
from Codebase.Variables import DataBasePath
ConnectionObject=sqlite3.connect(DataBasePath)
def ExecuteCommand(cmd,iterable=None):
    global ConnectionObject
    cursor=ConnectionObject.cursor()
    if iterable==None:
        result=cursor.execute(cmd)
    else:
        result=cursor.execute(cmd,iterable)
    result=result.fetchall()
    ConnectionObject.commit()
    return result

def ExecuteManyCommands(cmd,iterable=None):
    global ConnectionObject
    cursor=ConnectionObject.cursor()
    if iterable==None:
        result=cursor.executemany(cmd)
    else:
        result=cursor.executemany(cmd,iterable)
    result=result.fetchall()
    ConnectionObject.commit()
    return result

def ExecuteScript(cmd):
    global ConnectionObject
    cursor=ConnectionObject.cursor()
    result=cursor.executescript(cmd)
    result=result.fetchall()
    ConnectionObject.commit()
    return result

def CloseConnection():
    global ConnectionObject
    ConnectionObject.close()
    ConnectionObject=None


