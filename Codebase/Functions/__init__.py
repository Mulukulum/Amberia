def ExecuteCommand(cmd):
    import sqlite3
    from Codebase.Variables import DataBasePath
    con=sqlite3.connect(DataBasePath)
    cursor=con.cursor()
    res=cursor.execute(cmd)
    con.commit()
    con.close()
    return res.fetchall()

def ExecuteManyCommands(cmd,iterable):
    import sqlite3
    from Codebase.Variables import DataBasePath
    con=sqlite3.connect(DataBasePath)
    cursor=con.cursor()
    res=cursor.executemany(cmd,iterable)
    con.commit()
    con.close()
    return res.fetchall()

def ExecuteScript(cmd):
    import sqlite3
    from Codebase.Variables import DataBasePath
    con=sqlite3.connect(DataBasePath)
    cursor=con.cursor()
    res=cursor.executemany(cmd)
    con.commit()
    con.close()
    return res.fetchall()





