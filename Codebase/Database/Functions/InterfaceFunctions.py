def IDGenerator():
    from random import randint
    result=randint(1,100_000_000)
    while ValidateID(result)!=True:             #While the ID is invalid
        result=randint(1,100_000_000)
    return result

def ValidateID(no):
    return True

def MainExecutor(con,cmd,iter=None):
    if iter!=None:
        for i in iter:
            res=con.execute(cmd,i)
    else:
        res=con.execute()
    return res.fetchall()

