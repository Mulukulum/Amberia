from Codebase.ErrorLogs.logging import CreateLog
#This Class defines a Priority Object
#Each task contains one of these, each object has a prioritylevel and a color associated with it
#There can be a maximum of 10 priority levels, where 10 is the lowest and 1 in the highest

class Priority: 
    
    ValidPriorites=(1,2,3,4,5,6,7,8,9,10)                 #Sets a tuple containing whole numbers from 1 to 10
                  
    @classmethod
    def IsValidPriority(cls,PrLevel) -> bool :     #Class method that ensures priority level call is valid
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
        return f'Priority Level {self.PriorityLevel}'
    
    #This classmethod returns the color of a priority level as an integer

    @classmethod
    def GetColor(cls,PrLevel) -> int :
        if cls.IsValidPriority(PrLevel)==False:          #If Priority is invalid, return None
            
            return None
        from csv import reader,QUOTE_NONE
        QUOTE_NONE                                          #Instructing the reader to Quote Nothing
        from os import path                                 #To Get the Path of the directory where code is stored
        FilePath=path.dirname(__file__) + '\\Priority.csv'  #This gets the path of the csv file
        with open(FilePath,'r+') as CSVFile:                
            Reader=reader(CSVFile                           #Opens the CSV File
            ,delimiter=','
            ,skipinitialspace=True)
            try:
                Color= list(Reader)[PrLevel]                #This gets the color that is stored as an integer
            except IndexError:
                #Place for ErrorLog Function Call
                return None
        return Color
    
    #Method to update priority level of priority object
    def UpdatePriorityLevel(self,NewLevel):
        if self.IsValidPriority(NewLevel) :
            self.PriorityLevel=NewLevel 
            ...                                   #This updates the color as well (this i'm not doing rn because we haven't setup sql)
        else:
            return False
        return True

    
        