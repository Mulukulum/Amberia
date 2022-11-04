from Codebase.ErrorLogs.logging import ErrorLog
from Codebase.Functions.Database import ExecuteCommand,ExecuteScript            
from Codebase.SQLScripts import ScriptSetDefaultColors,DefaultPriorityColors
#This Class defines a Priority Object
#Each task contains one of these, each object has a prioritylevel and a color associated with it
#There can be a maximum of 10 priority levels, where 10 is the lowest and 1 in the highest
class Priority: 
    ColorCache=dict()                                           #Creates the Dictionary used for Cacheing
    Resultant=ExecuteCommand("""SELECT * FROM prcolors;""")     #Gets the current values from the Database
    if Resultant==[]:                                           #If the database is empty
        ExecuteScript(ScriptSetDefaultColors)           #Runs the script to set the default colors
        ColorCache=DefaultPriorityColors.copy()         #Updates the Cache
    ColorCache.update(Resultant)
    del Resultant                                       #Deletes the resultant list because its not needed

    @classmethod
    def IsValidPriority(cls,PrLevel: int) -> bool :     #Class method that ensures priority level call is valid
        ValidPriorites=(1,2,3,4,5,6,7,8,9,10)      #Sets a tuple containing whole numbers from 1 to 10
        if PrLevel in ValidPriorites:
            return True
        else: return False
    
    #Initialising class
    def __init__(self,PriorityLevel=10) -> None:
        self.PriorityLevel=PriorityLevel
        self.Color=self.GetColor(PriorityLevel)

    #Class Representation    
    def __repr__(self) -> str:
        return f'Priority({self.PriorityLevel})'
    
    def __str__(self) -> str:
        return f'Priority Level {self.PriorityLevel}\nColor {self.Color}'
    
    '''
    Default Colors as integers
    Colors={
    1:16399941,
    2:16070549,
    3:8069048,
    4:9201120,
    5:2287801,
    6:5177211,
    7:432432,
    8:13419293,
    9:16729344,
    10:16249827,
}
    '''

    @classmethod
    def GetColor(cls,PrLevel: int) -> str :
        if cls.IsValidPriority(PrLevel)==False:          #If Priority is invalid, return None
            ErrorLog(f"Unable to get Priority Color due to Invalid Priority Level input {PrLevel}")
            return None
        if PrLevel in cls.ColorCache:                       #If the ""cache"" already has this,
            return cls.ColorCache[PrLevel]                  #then return the cached value
        try:
            ErrorLog(f"TRIVIAL WARNING: NoValueInCache for Priority Level {PrLevel}")
            ResultantList=ExecuteCommand("""SELECT clrvalue FROM prcolors where level=?;""",(PrLevel,))
            return ResultantList[0][0]  #The [0][0] part escapes the list and the tuple to give only the integer
        except IndexError:  #This Happens when the database is empty, and an empty list is returned
            ErrorLog("GetColor Method called without initialisation of prcolors")
            ExecuteScript(ScriptSetDefaultColors)           #Runs the script to set the default colors
            cls.ColorCache=DefaultPriorityColors.copy()     #Updates the Cache
            return cls.ColorCache[PrLevel]                  #Returns the default color

    #Method to update priority level of priority object
    def UpdatePriorityLevel(self,NewLevel: int) -> bool :
        if self.IsValidPriority(NewLevel) :
            self.PriorityLevel=NewLevel           #Enforcing an official unofficial rule that:
            self.Color=self.ColorCache[NewLevel]  #ColorCache must always be populated
        else:
            return False
        return True
    
    @classmethod
    def FlushToCache(cls) -> None:      #Forcibly updates the current color values into cache
        Resultant=ExecuteCommand("""SELECT * FROM prcolors;""")
        cls.ColorCache.update(Resultant)

    @classmethod
    def UpdateColor(cls,PrLevel: int,NewColor: int) -> None:
        if cls.IsValidPriority(PrLevel)==False:
            return False
        NewColor=abs(NewColor)          #Optional Line to ensure negatives don't mess stuff up
        cls.ColorCache[PrLevel]=NewColor        #Updates the Cache with the new value
        ExecuteCommand("UPDATE prcolors SET clrvalue=? WHERE level=?;",(NewColor,PrLevel)) #Updates the database with the new values
        return True