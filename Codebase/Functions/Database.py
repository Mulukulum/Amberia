import datetime
import sqlite3                                      
from Codebase.Variables import DataBasePath         #Get the location of the Database
ConnectionObject=sqlite3.connect(DataBasePath,detect_types=sqlite3.PARSE_COLNAMES|sqlite3.PARSE_DECLTYPES)      #Creates the connection to the databse

def UDF() -> None:                                          #Function to call the UserDefinedFunctions
    global ConnectionObject
    ConnectionObject.create_function(name="HexFormat",narg=1,func=HexFormat,deterministic=True)
    ConnectionObject.create_function(name='CheckIfToday',narg=1,func=CheckIfToday,deterministic=False)

def HexFormat(number: int) -> str:
    number=abs(number)          #Line to ensure someone that negative values don't mess stuff up
    if number>=16777214:        #If the number is too big just return White
        return  "#FFFFFF"
    #This next bit takes the hex value and removes the starting 0x bit added by python
    #Uppercase that and make it have a length of 6 using the .rjust() method
    hexcode=hex(number)[2::].upper().rjust(6,"0")       
    return "#"+hexcode

def CheckIfToday(Date:datetime.datetime):
    if Date==None: return 0
    if type(Date)==type('String'):
        Date=datetime.datetime.strptime(Date[0:19],"%Y-%m-%d %X")
    if datetime.date.today()==Date.date():
        return 1
    else:
        return 0


UDF()                                                   #Defines the functions

#Main Functions used to query the DB:

def ExecuteCommand(cmd: str,iterable=None) -> list:     #Takes a cmd string and an optional iterable to replace a placeholder
    global ConnectionObject
    cursor=ConnectionObject.cursor()                    #Creates cursor object
    if iterable==None:
        result=cursor.execute(cmd)
    else:
        result=cursor.execute(cmd,iterable)
    result=result.fetchall()                        #Fetches results
    ConnectionObject.commit()                       #Commits the database
    return result                                   #Returns the list
    
def ExecuteManyCommands(cmd: str,iterable=None) -> list:          #Takes a cmd string and an optional iterable for placeholders
    global ConnectionObject                             
    cursor=ConnectionObject.cursor()                #Creates cursor object
    if iterable==None:
        result=cursor.executemany(cmd)
    else:
        result=cursor.executemany(cmd,iterable)
    result=result.fetchall()                        #Fetches results
    ConnectionObject.commit()                       #Commits the database
    return result                                   #Returns the list

def ExecuteScript(cmd: str) -> list:
    global ConnectionObject
    cursor=ConnectionObject.cursor()                #Creates cursor
    result=cursor.executescript(cmd)                #Executes the script
    result=result.fetchall()                        #Returns the list
    ConnectionObject.commit()                       #Commits changes
    return result                                   #Returns the list

def CloseConnection() -> None:
    global ConnectionObject     
    ConnectionObject.close()                        #Closes the connection
    ConnectionObject=None                           #Sets the conn


