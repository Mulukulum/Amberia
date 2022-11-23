#Required imports
#Importing all the log functions
from Codebase.ErrorLogs.logging import ErrorLog,Log,DBLog,DBOnlyLog

#Importing functions to interface with the database
from Codebase.Functions.Database import ExecuteCommand,ExecuteScript            

#Importing The Required Colors for Labels
from Codebase.Functions.Colors import GetRandomColor

class Project:
    def __init__(self, Name, Color=None, Projects = list(), ParentProjects = list()):
        self.Name = Name                 #Initialize name of project
        self.Color = Color               #Initialize display color
        self.Sections = list()               #Initialize list of sections
        DefaultSection = Section(f"_{self.Name}")
        DefaultSection.SetProject(self)
        self.Sections.append(DefaultSection)
        self.SubProjects = Projects           #Initialize list of sub projects 
        self.parentprojects = ParentProjects  #Initialize list of parent projects 

    def SetName(self, name):                 #Set name of project
        self.Name = name

    def SetColor(self, color):
        self.Color = color

    def AddSection(self, newsection):
        self.Sections.append(newsection)

    def RemoveSection(self, delsection):
        self.Sections.remove(delsection)

    def AddProject(self, newproject):
        self.SubProjects.append(newproject)

    def RemoveProject(self, delproject):
        self.SubProjects.remove(delproject)

    def AddParentProject(self, newparent):
        self.parentprojects.append(newparent)

    def RemoveParentProject(self, delparent):
        self.parentprojects.remove(delparent)

    def DisplaySections(self):
        print(*self.Sections,sep='\n')

    def DisplayProjects(self):
        print(*self.SubProjects,sep='\n')

    def DisplayParentProjects(self):
        print(*self.parentprojects,sep='\n')
          

    def __str__(self):
        return  f'Project name: {self.Name} \
                \nDisplay color: {self.Color} \
                \nSections: {[str(s) for s in self.Sections]}'

    def __repr__(self):
        return f"Project({self.Name},{self.Color},{self.Sections},{self.SubProjects},{self.parentprojects})"

class Section:
    def __init__(self, Name, Project: Project, Tasks: list=list()):
        self.Name = Name                 #Initialize name of section
        self.Project = Project
        self.Tasks = Tasks               #Initialize a list of tasks

    def SetProject(self, NewProject):   #Set the project to which the section belongs
        self.Project = NewProject         

    def AddTask(self, NewTask):         #Add a new task to the section
        self.Tasks.append(NewTask)

    def RemoveTask(self, DelTask):      #Remove a task from the list of tasks
        self.Tasks.remove(DelTask)

    def DisplayTasks(self):             #Display the list of tasks
        print(*self.Tasks,sep='\n')      #Displays tasks without a for loop         

    def __repr__(self):
        return f"Section({self.Name},{self.Project},{self.Tasks})"              

    def __str__(self):
        return f'Section name: {self.Name} \nProject name: {self.Project.name} \nTasks: {[str(t) for t in self.Tasks]}'        
        #fstring returns the string representation

class Label:

    #Class initialisation | Method returns True if Creation was successful
    def __init__(self, Title : str ,Color : int=None) -> bool:

        if Label.LabelExists(Title):
            #If the Label already exists, then Log an Error
            ErrorLog(f" TRIVIAL : Attempt to create label {Title} which already exists")
            return False

        else:
            self.Title=Title                #Set Title
            if Color==None:                 #If there is no Color specified 
                self.Color=GetRandomColor() #Pick a random Color

            else:
                #Set the specified Color
                self.Color=Color

            ExecuteCommand("INSERT INTO labels(title,color,taskcount) VALUES(?,?,0) ;",(self.Title,self.Color))
            return True
        
    #Method to check whether a label currently exists
    @staticmethod
    def LabelExists(LabelTitle) -> bool:

        #Find the label
        #If it doesn't exist, return False
        
        if ExecuteCommand("SELECT title FROM labels WHERE title=?",(LabelTitle,))==[]:
            return False
        else:
            return True

    #Method to change the color of a label
    def SetColor(self,Color: int) -> None :

        if Color>=16777214:
            self.Color=Color

        else:
            self.Color=16777214
            ErrorLog(f" TRIVIAL : DEFAULT SET DUE TO Invalid Color Assignment ({Color}) for Label {self.Title}")

    def RandomizeColor(self) -> None:
        self.Color=GetRandomColor()

    #Label repr 
    def __repr__(self) -> str:
        return f'Label({self.Title},{self.Color})'
    
    #String Representation
    def __str__(self) -> str:
        return f'Label {self.Title} Color {self.Color}'



#This Class defines a Priority Object
#Each task contains one of these, each object has a prioritylevel and a color associated with it
#There can be a maximum of 10 priority levels, where 10 is the lowest and 1 in the highest
class Priority: 

    ColorCache=dict()                                           #Creates the Dictionary used for Cacheing
    Resultant=ExecuteCommand("""SELECT * FROM prcolors;""")     #Gets the current values from the Database

    if Resultant==[]:                                           #If the database is empty

        #Imports the necessary script and Priority colors
        from Codebase.SQLScripts import ScriptSetDefaultColors
        from Codebase.SQLScripts import DefaultPriorityColors
        
        ExecuteScript(ScriptSetDefaultColors)           #Runs the script to set the default colors
        ColorCache=DefaultPriorityColors.copy()         #Updates the Cache
    
    ColorCache.update(Resultant)
    del Resultant                                       #Deletes the resultant list because its not needed

    #Class method that ensures priority level call is valid
    @classmethod
    def IsValidPriority(cls,PrLevel: int) -> bool :     
        ValidPriorites=(1,2,3,4,5,6,7,8,9,10)     #Sets a tuple containing whole numbers from 1 to 10
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

    #Method to get the Color of a Priority Level
    @classmethod
    def GetColor(cls,PrLevel: int) -> str :

        #If Priority is invalid, return None
        if cls.IsValidPriority(PrLevel)==False:          
            ErrorLog(f"Unable to get Priority Color due to Invalid Priority Level input {PrLevel}")
            return None

        #If the ""cache"" already has this,
        if PrLevel in cls.ColorCache:
            return cls.ColorCache[PrLevel]      #then return the cached value
        
        #If its not in the cache then something has gone wrong somewhere,hence the TRIVIAL WARNING
        ErrorLog(f"TRIVIAL WARNING: NoValueInCache for Priority Level {PrLevel}")
        ResultantList=ExecuteCommand("""SELECT clrvalue FROM prcolors where level=?;""",(PrLevel,))

        try:
            return ResultantList[0][0]  #The [0][0] part escapes the list and the tuple to give only the integer

        except IndexError:  
            
            #This Happens when the database is empty, and an empty list is returned
            from Codebase.SQLScripts import ScriptSetDefaultColors,DefaultPriorityColors
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
    
    #Forcibly updates the current color values into cache
    @classmethod
    def FlushToCache(cls) -> None:      #Forcibly updates the current color values into cache
        Resultant=ExecuteCommand("SELECT * FROM prcolors;")
        cls.ColorCache.update(Resultant)

    @classmethod
    def UpdateColor(cls,PrLevel: int,NewColor: int) -> bool:
        
        if cls.IsValidPriority(PrLevel)==False:
            return False

        NewColor=abs(NewColor)          #Optional Line to ensure negatives don't mess stuff up
        cls.ColorCache[PrLevel]=NewColor        #Updates the Cache with the new value
        
        ExecuteCommand("UPDATE prcolors SET clrvalue=? WHERE level=?;",(NewColor,PrLevel)) #Updates the database with the new values
        return True
    
    #Fast methods
    # Don't use these methods unless you know the input is 
    # going to be a perfectly correct one

    @classmethod
    def GetColorFast(cls,PrLevel: int) -> str :
        return cls.ColorCache[PrLevel]                  #Returns the default color
    
    @classmethod
    def UpdateColorFast(cls,PrLevel: int,NewColor: int) -> None:
        cls.ColorCache[PrLevel]=NewColor        #Updates the Cache with the new value
        ExecuteCommand("UPDATE prcolors SET clrvalue=? WHERE level=?;",(NewColor,PrLevel)) #Updates the database with the new values
        return True
    
    def UpdatePriorityLevelFast(self,NewLevel: int) -> None :
        self.PriorityLevel=NewLevel           #Enforcing an official unofficial rule that:
        self.Color=self.ColorCache[NewLevel]  #ColorCache must always be populated

class Task:
    def __init__(self, TaskTitle, TaskDesc=None, PriorityLevel=10, DueDate=None, Labels=None): #Initializes the class
        self.TaskTitle=TaskTitle
        self.TaskDesc=TaskDesc
        self.DueDate=DueDate
        if Priority.IsValidPriority(PriorityLevel):          #Checks if the incoming argument is a valid priority level
            self.priority=Priority(PriorityLevel)            #If so, then give the task its priority
        else:
            self.priority=Priority(10)                  #If not, then set it to a default value of 10
            Log(f"Task {self.TaskTitle} given no priority. Default Value Assigned")

        if Labels==None:                                #Checks if any labels are selected
            self.Labels=[]                              #Makes it an empty list instead of None
        else: 
            self.Labels=Labels                          #Makes a list of the selected labels

    def ToggleLabel(self,NewLabel):
        if NewLabel in self.Labels:                     #Checks if the label is already selected
            self.Labels.remove(NewLabel)                #Removes the label if it is already selected
        else: 
            self.Labels.append(NewLabel)                #Adds the label if it isnt selected

    def __repr__(self):                         
        return f"task('{self.TaskTitle}','{self.TaskDesc}',{self.priority},{self.DueDate},{self.Labels})" 
        #Repr returns how to create the task
