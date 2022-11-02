import sqlite3
from time import sleep

ShutDownRequest=False #Flag used to signal when to stop

def ActivateDatabase():
    from Codebase.Database import DataBasePath


def ReadDB(con,cmd):
    try:
        res=con.execute(cmd).fetchall()
        con.commit()
    except:
        return -1
    else:
        return res

def _ShutDown(con):
    ...
    