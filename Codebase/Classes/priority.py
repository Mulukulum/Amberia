




#This Class defines a Priority Object
#Each task contains one of these, each object has a prioritylevel and a color associated with it
#There can be a maximum of 10 priority levels, where 10 is the lowest and 1 in the highest

class Priority:
    #Sets a tuple containing whole numbers from 1 to 10 
    ValidPriorites=(x+1 for x in range(10))
    
    #Initialising class
    def __init__(self,PriorityLevel=10) -> None:
        self.PriorityLevel=PriorityLevel

    #Class Representation    
    def __repr__(self) -> str:
        return f'Priority Level {self.PriorityLevel}'
    
    #This classmethod returns the color of a priority level 

    @classmethod
    def GetColor(cls,PrLevel) -> int :
        import csv
        from os import path #To Get the Path of the directory where code is stored
        FilePath=path.dirname(__file__) + '\\Priority.csv'  #This gets the path of the csv file
        csv.QUOTE_NONE #Instructing the reader to Quote Nothing
        with open(FilePath,'r+') as CSVFile:
            Reader=csv.reader(CSVFile,delimiter=',',skipinitialspace=True)
            L=list(Reader)


    #Method to update priority level of said priority object
    def UpdatePriorityLevel(self,NewLevel):
        if NewLevel in Priority.ValidPriorities:
            self.PriorityLevel=NewLevel 
            ...                                #This updates the color as well
        else:
            return False
        return True
Priority.GetColor(2)
    
        