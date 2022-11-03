def ExecuteCommand(cmd,iterable):
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

def ExecuteManyCommands(cmd,iterable):
    import sqlite3
    from Codebase.Variables import DataBasePath
    con=sqlite3.connect(DataBasePath)
    cursor=con.cursor()
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
    res=cursor.executemany(cmd)
    res=res.fetchall()
    con.commit()
    con.close()
    return res




