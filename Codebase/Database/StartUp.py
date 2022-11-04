
#The following function checks if a table exists in a database
def CheckAndCreate(cur,name: str,attributes: str):
    cur.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{name}';""")  #Checks if the table exists
    if cur.fetchall()==[]:              #If No matches were found, (i.e table doesn't exist)
        if _CreateTable(cur,name,attributes)==True:
            return True
        else:
            return False
    else:
        return True                     #return True if the table exists

#Function to create a table
def _CreateTable(cur,name: str,attributes: str):
    try:
        cur.execute(f"""CREATE TABLE {name}({attributes});""")
        return True
    except:
        return False


