def ExecuteCommand(cmd,iterable=None):
    import sqlite3
    from Codebase.Variables import DataBasePath
    con=sqlite3.connect(DataBasePath)
    cursor=con.cursor()
    if iter==None:
        res=cursor.execute(cmd)
    else:
        res=cursor.execute(cmd,iterable)
    res=res.fetchall()
    con.commit()
    con.close()
    return res

def ExecuteManyCommands(cmd,iterable=None):
    import sqlite3
    from Codebase.Variables import DataBasePath
    con=sqlite3.connect(DataBasePath)
    cursor=con.cursor()
    if iter==None:
        res=cursor.executemany(cmd)
    else:
        res=cursor.executemany(cmd,iterable)
    res=res.fetchall()
    con.commit()
    con.close()
    return res

def ExecuteScript(cmd):
    import sqlite3
    from Codebase.Variables import DataBasePath
    con=sqlite3.connect(DataBasePath)
    cursor=con.cursor()
    res=cursor.executescript(cmd)
    res=res.fetchall()
    con.commit()
    con.close()
    return res




