def IDGenerator():
    from random import randint
    result=randint(1,100_000_000)
    while ValidateID(result)!=True:             #While the ID is invalid
        result=randint(1,100_000_000)
    return result

def ValidateID(no):
    return True

def MainExecutor(con,cmd):
    con.execute(cmd)
    ...