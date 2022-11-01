
from Codebase.Database import DataBasePath
#The following function checks if a table exists in a database
def CheckAndCreate(cur,name,attributes):
    cur.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{name}';""")  #Checks if the table exists
    if cur.fetchall()==[]:              #If No matches were found, (i.e table doesn't exist)
        if _CreateTable(cur,name,attributes)==None:
            return True
    else:
        return True                     #return True if the table exists

#Function to create a table
def _CreateTable(cur,name,attributes):
    try:
        cur.execute(f"""CREATE TABLE {name}({attributes});""")
    except:
        return False


