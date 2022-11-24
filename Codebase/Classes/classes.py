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

    #Necessary Variable Declarations
    UpperBound=10
    ValidPriorites=tuple(range(1,UpperBound+1))     
    #Sets a tuple containing the valid priority Levels
    #Tuple contains integers from 1 to Upperbound (1 to 10)
    DefaultPriorityColors={
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
    ScriptSetDefaultColors=f"""
    -- The Following Commands sets the Default Colors again
    BEGIN;
    -- DELETE ALL THE VALUES IN THE TABLE
    DELETE FROM prcolors;

    -- Now Insert the Values into the table 
    INSERT INTO prcolors (level,clrvalue) VALUES {f'{list(DefaultPriorityColors.items())}'.strip('[]')} ;
    END;
    """

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
    def IsValid(cls,PrLevel: int) -> bool :      

        if PrLevel in cls.ValidPriorites:    return True
        else:                            return False

    #Method to get the Color of a Priority Level
    @classmethod
    def ColorOfLevel(cls,PrLevel: int) -> str :

        #If Priority is invalid, return None
        if cls.IsValid(PrLevel)==False:          
            ErrorLog(f"Unable to get Priority Color due to Invalid Priority Level input {PrLevel}")
            return None

        #If the ""cache"" already has this,
        if PrLevel in cls.ColorCache:

            #then return the cached value
            return cls.ColorCache[PrLevel]      
        
        #If its not in the cache then something has gone wrong somewhere,hence the TRIVIAL WARNING
        ErrorLog(f"TRIVIAL WARNING: NoValueInCache for Priority Level {PrLevel}")
        ResultantList=ExecuteCommand("""SELECT clrvalue FROM prcolors where level=?;""",(PrLevel,))
        return ResultantList[0][0]  #The [0][0] part escapes the list and the tuple to give only the integer
    

    #Forcibly updates the current color values into cache
    @classmethod
    def FlushToCache(cls) -> None:      #Forcibly updates the current color values into cache
        Resultant=ExecuteCommand("SELECT * FROM prcolors;")
        cls.ColorCache.update(Resultant)

    @classmethod
    def UpdateColor(cls,PrLevel: int,NewColor: int) -> bool:
        
        if cls.IsValid(PrLevel)==False:
            return False

        NewColor=abs(NewColor)          #Optional Line to ensure negatives don't mess stuff up
        cls.ColorCache[PrLevel]=NewColor        #Updates the Cache with the new value
        
        ExecuteCommand("UPDATE prcolors SET clrvalue=? WHERE level=?;",(NewColor,PrLevel)) #Updates the database with the new values
        return True






class Task:

    Instances=dict()

    def __init__(self, TaskTitle: str, TaskDesc: str='', PriorityLevel: int=10, DueDate: datetime.datetime=None): #Initializes the class

        #Sets the Title and Description for the task
        self.TaskTitle=TaskTitle
        self.TaskDesc=TaskDesc

        self.DueDate=DueDate
        self.Completed=0                                #sets completed to False, sql doesn't have bool so I'm using 0 and 1
        self.CompletedDate=None                         #makes the object for completed date

        #Priority Level of Task

        if Priority.IsValid(PriorityLevel):          #Checks if the incoming argument is a valid priority level
            self.PriorityLevel=PriorityLevel         #If so, then give the task its priority level
        else:
            self.PriorityLevel=Priority.UpperBound   #If not, then set it to a default upperbound value
            Log(f"Task {self.TaskTitle} given no priority. Default Value {self.PriorityLevel} Assigned")

        self.Color=Priority.ColorOfLevel(PriorityLevel)     #And assign the color as well
        
        #ID of Task
        self.ID=ExecuteCommand(f"""INSERT INTO  RETURNING taskid;""")[0][0]
        
        #Makes the List of labels assigned to the task
        self.Labels=[]

        #Add the task to the dictionary of instances
        Task.Instances[self.ID]=self

    def ToggleLabel(self,Label):
        if Label in self.Labels:
            ...
            #Remove the label from the task
        else:
            self.AddLabel(Label)

    def AddLabel(self,NewLabel):
        
        ScriptToAddLabelToTask=f"""
        --This Script adds A Label to the Task
        BEGIN;
        --
        """

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
        if Priority.IsValid(priority):          #Checks if the incoming argument is a valid priority level
            self.PriorityLevel=Priority(priority)            #If so, then give the task its new priority
        if Labels!=None:
            self.AddLabel(Labels)
        ExecuteCommand(f"update tasks set title={self.TaskTitle},task_desc={self.TaskDesc}, due_date={self.DueDate}, priority={self.PriorityLevel.PriorityLevel}, labels={self.Labels} where taskid={TaskID}")
    def complete(self, TaskID):
        self.Completed=1                                #completes the task
        self.CompletedDate=datetime.datetime.now()      #records the completed time
        ExecuteCommand(f"update tasks set completed={self.Completed}, completed_date={self.CompletedDate} where taskid={TaskID}")

    def change_due_date(self, NewDueDate, TaskID):
        self.DueDate=NewDueDate                         #accepts a new due date
        ExecuteCommand(f"update tasks set due_date={self.DueDate} where taskid={TaskID}")
    
    #Update the PriorityLevel of the Task

    def UpdatePriority(self, priority: int):
        if Priority.IsValid(priority):                      #Checks if the incoming argument is a valid priority level
            self.PriorityLevel=Priority(priority)           #If so, then give the task its new priority
            self.Color=Priority.ColorOfLevel(priority)      #Give the task its new color
            ExecuteCommand(f"UPDATE tasks SET task_priority=? WHERE task_id=?",(self.PriorityLevel,self.ID))
            

    def __repr__(self):                         
        return f"task('{self.TaskTitle}','{self.TaskDesc}',{self.PriorityLevel},{self.DueDate},{self.Labels})" 
        #Repr returns how to create the task
