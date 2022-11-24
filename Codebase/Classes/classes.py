#Required imports
#Importing all the log functions
from Codebase.ErrorLogs.logging import ErrorLog,Log,DBLog,DBOnlyLog

#Importing functions to interface with the database
from Codebase.Functions.Database import ExecuteCommand,ExecuteScript            

#Importing The Required Colors for Labels
from Codebase.Functions.Colors import GetRandomColor

import datetime

class Project:
    
    #Empty dictionary to store the instances of all the projects
    Instances=dict()

    def __init__(self, ProjectTitle, ProjectColor: int=None):

        self.Title = ProjectTitle                 #Initialize name of project
        
        #Set a random color if No Color was specified or the Color is Invalid
        if ProjectColor==None or ProjectColor<=16777215:
            self.Color=GetRandomColor()
        else:
            self.Color=ProjectColor

        #Add the Project to the Database
        self.ID=ExecuteCommand(
        """
        INSERT INTO 
        projects(
        project_title, 
        project_color,
        project_sectioncount
        ) 
        VALUES(?,?,?)
        RETURNING project_id
        """,
        (self.Title, #Project Title
        self.Color,  #Section Count
        0
        )
        )[0][0]         #The [0][0] part escapes the list giving us the id alone
        
        #Add the project to the dictionary of instances
        Project.Instances[self.ID]=self

        #Setting up the Default Section of the Project: 
        #Create and Set the DefaultSection
        self.DefaultSection = Section(SectionProject=self , SectionTitle=f"_{self.Title}",DefaultSection=True)

        #Create the List of Sections
        self.Sections=[self.DefaultSection,]

    #Method to set a New name for the Project
    def SetName(self, NewName: str):                 
        self.Title = NewName            #Set name of project
        ExecuteCommand("UPDATE projects SET project_title=? WHERE project_id=?",
                        (NewName,self.ID))
    
    #Method to set a new color for the project
    def SetColor(self, Color: int):
        if Color<=16777215:
            self.Color = Color
            ExecuteCommand("UPDATE projects SET project_color=? WHERE project_id=?",
                            (self.Color,self.ID))
    
    #Use this if you're feeling lucky
    def RandomizeColor(self):
        self.Color=GetRandomColor()
        ExecuteCommand("UPDATE projects SET project_color=? WHERE project_id=?",
                        (self.Color,self.ID))


    #Method to add a new section to a project
    def AddSection(self,SectionTitle: str): #Takes the Name of the Section as input
        
        #Create and append the Section to the list of sections
        self.Sections.append(
            Section(SectionProject=self,SectionTitle=SectionTitle)
            )
        #Update the sectioncount attribute
        ExecuteCommand("UPDATE projects SET project_sectioncount=project_sectioncount+1 WHERE project_id=?",(self.ID,))

    def RemoveSection(self, SectionID: int):
        ...

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
        return  f'Project name: {self.Title} \
                \nDisplay color: {self.Color} \
                \nSections: {[str(s) for s in self.Sections]}'

    def __repr__(self):
        return f"Project({self.Title},{self.Color},{self.Sections},{self.SubProjects},{self.parentprojects})"



class Section:
    
    #Dictionary to store the instances of all available Section objects
    Instances=dict()

    def __init__(self,SectionProject: Project, SectionTitle: str, DefaultSection=False):
        
        #Check Validity of The section Title
        #Ensuring that SectionTitle's can't start with a single underscore followed by characters
        if SectionTitle[0]=="_" and DefaultSection==False :
            self.Title=(f"__{SectionTitle.strip('_')}__")   #Sets Title to __sectionname__
        self.Project = SectionProject    #Get the Parent Project

        #Add the Section to the Database
        self.ID=ExecuteCommand(
        """
        INSERT INTO sections
        (section_parentprojectid,
        section_title,
        section_taskcount
        )
        VALUES (?,?,?)
        RETURNING section_id
        """,
        (self.Project.ID, #ID of the parentProject
        self.Title,       #Title of the Section
        0                 #New section so no tasks added
        )
        )[0][0]             
        
        #Add the section to the List of instances
        Section.Instances[self.ID]=self

    def AddTask(self, NewTask):         #Add a new task to the section
        ExecuteCommand("UPDATE sections SET section_taskcount=section_taskcount+1 WHERE section_id=?",(self.ID))

    def RemoveTask(self, DelTask):      #Remove a task from the list of tasks
        self.Tasks.remove(DelTask)
        ExecuteCommand("UPDATE sections SET section_taskcount=section_taskcount-1 WHERE section_id=?",(self.ID))

    def DisplayTasks(self):             #Display the list of tasks
        print(*self.Tasks,sep='\n')      #Displays tasks without a for loop         

    def __repr__(self):
        return f"Section({self.Title},{self.Project},{self.Tasks})"              

    def __str__(self):
        return f'Section name: {self.Title} \nProject name: {self.Project.name} \nTasks: {[str(t) for t in self.Tasks]}'        
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

            ExecuteCommand("INSERT INTO labels(label_title,label_color,label_taskcount) VALUES(?,?,0) ;",(self.Title,self.Color))
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

        if Color>=16777215:
            self.Color=Color

        else:
            self.Color=16777215
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

    def __init__(self, TaskTitle, TaskDesc=None, priority=None, DueDate=None, Labels=list()): #Initializes the class
        self.TaskTitle=TaskTitle
        self.TaskDesc=TaskDesc
        self.DueDate=DueDate
        self.Completed=0                                #sets completed to False, sql doesn't have bool so I'm using 0 and 1
        self.CompletedDate=None                         #makes the object for completed date
        if Priority.IsValidPriority(priority):          #Checks if the incoming argument is a valid priority level
            self.priority=Priority(priority)            #If so, then give the task its priority
        else:
            self.priority=Priority(10)                  #If not, then set it to a default value of 10
            Log(f"Task {self.TaskTitle} given no priority. Default Value Assigned")
        self.Labels=Labels
        self.id=ExecuteCommand(f"INSERT INTO tasks(title, task_desc, priority, due_date, completed) values ({self.TaskTitle},{self.TaskDesc},{self.priority},{self.DueDate},{self.Completed}) RETURNING taskid;")[0][0]

    def set_label(self,NewLabel, TaskID):
        if NewLabel in self.Labels:                     #Checks if the label is already selected
            self.Labels.remove(NewLabel)                #Removes the label if it is already selected
        else: 
            self.Labels.append(NewLabel)                #Adds the label if it isnt selected
        ExecuteCommand(f"update tasks set labels={self.Labels} where taskid={TaskID}")

    def reconfigure(self, TaskID, TaskTitle=None, TaskDesc=None, priority=None, DueDate=None, Labels=None):
        if TaskTitle!=None:
            self.TaskTitle=TaskTitle                    #Changes the title to a newly provided title, if not provided stays the same
        if TaskDesc!=None:
            self.TaskDesc=TaskDesc                      #Changes the desc to a newly provided desc
        else:
            self.TaskDesc=None                          #makes task desc null if not provided
        if DueDate!=None:
            self.DueDate=DueDate                        #Changes the due date to a newly provided due date
        else:
            self.DueDate=None                           #makes due date null if none provided
        if Priority.IsValidPriority(priority):          #Checks if the incoming argument is a valid priority level
            self.priority=Priority(priority)            #If so, then give the task its new priority
        if Labels!=None:
            self.set_label(Labels)
        ExecuteCommand(f"update tasks set title={self.TaskTitle},task_desc={self.TaskDesc}, due_date={self.DueDate}, priority={self.priority.PriorityLevel}, labels={self.Labels} where taskid={TaskID}")
    def complete(self, TaskID):
        self.Completed=1                                #completes the task
        self.CompletedDate=datetime.datetime.now()      #records the completed time
        ExecuteCommand(f"update tasks set completed={self.Completed}, completed_date={self.CompletedDate} where taskid={TaskID}")

    def change_due_date(self, NewDueDate, TaskID):
        self.DueDate=NewDueDate                         #accepts a new due date
        ExecuteCommand(f"update tasks set due_date={self.DueDate} where taskid={TaskID}")
    
    def update_priority(self, priority, TaskID):
        if Priority.IsValidPriority(priority):          #Checks if the incoming argument is a valid priority level
            self.priority=Priority(priority)            #If so, then give the task its new priority
        ExecuteCommand(f"update tasks set priority={self.priority.PriorityLevel} where taskid={TaskID}")


    def __repr__(self):                         
        return f"task('{self.TaskTitle}','{self.TaskDesc}',{self.priority.PriorityLevel},{self.DueDate},{self.Labels})" 
        #Repr returns how to create the task
