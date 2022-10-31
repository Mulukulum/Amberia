
from Codebase.Database import DataBasePath
#The following function checks if a table exists in a database
def Check(cur,name):
    cur.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{name}';""")        #Checks if the table exists
    if cur.fetchall()==[]:              #If No matches were found, (i.e table doesn't exist)
        return False                    #return False
    else:
        return True                     #return True if the table exists

