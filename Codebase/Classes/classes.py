#Required imports
#Importing all the log functions
from Codebase.ErrorLogs.logging import ErrorLog,Log,DBLog,DBOnlyLog

#Importing functions to interface with the database
from Codebase.Functions.Database import ExecuteCommand,ExecuteScript     

import datetime

class Label:
    #Class initialisation
    def __init__(self,Title='',Color=None) -> None:
        self.Title=Title                    #Set the Title of the Label
        self.Color=Color
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
        from Codebase.SQLScripts import ScriptSetDefaultColors,DefaultPriorityColors
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
        except IndexError:  #This Happens when the database is empty, and an empty list is returned
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
        Resultant=ExecuteCommand("""SELECT * FROM prcolors;""")
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

class Section:
    
    def __init__(self, name, project=None, tasks=list()):

        self.name = name                 #Initialize name of section
        self.project = project
        self.tasks = tasks               #Initialize a list of tasks
        # Add new section to sections table
        self.id=ExecuteCommand("""INSERT INTO sections 
                (title, taskcount, parentprojectid) VALUES (?, ?, ?) RETURNING sectionid""",
                (self.name, len(self.tasks), self.project.id if project != None else 0))[0][0]
        

    def set_project(self, newproject):   #Set the project to which the section belongs
        self.project = newproject
        
        # Update parent project of section in sections table
        ExecuteCommand("UPDATE sections set parentprojectid = ? where sectionid = ?;", (newproject.id, self.id))
        
    def add_task(self, newtask):         #Add a new task to the section
        self.tasks.append(newtask)

        # Update taskcount of section in sections table
        ExecuteCommand("UPDATE sections set taskcount = ? where sectionid = ?;", (len(self.tasks), self.id))
        
    def remove_task(self, deltask):      #Remove a task from the list of tasks
        self.tasks.remove(deltask)

        # Update taskcount of section in sections table
        ExecuteCommand("UPDATE sections set taskcount = ? where sectionid = ?;", (len(self.tasks), self.id))

    def display_tasks(self):             #Display the list of tasks
        print(*self.tasks,sep='\n')      #Displays tasks without a for loop

    def __repr__(self):
        return f"Section({self.name},{self.project},{self.tasks})"              

    def __str__(self):
        return f'Section name: {self.name} \nProject name: {self.project.name} \nTasks: {[str(t) for t in self.tasks]}'        
        #fstring returns the string representation

class Project:

    def __init__(self, name, color, projects = list(), parentprojects = list(),sections=list()):
        self.name = name                 #Initialize name of project
        self.color = color               #Initialize display color
        self.sections = sections              #Initialize list of sections
        self.subprojects = projects           #Initialize list of sub projects 
        self.parentprojects = parentprojects  #Initialize list of parent projects
        
        # Add new project to projects table
        self.id=ExecuteCommand("INSERT INTO projects (title, color, sectioncount, projectcount) VALUES (?, ?, ?, ?) RETURNING id;",
                       (self.name, 
                       self.color, 
                       len(sections)+1, #Here, the +1 is for the default section thats yet to be appended
                       len(self.subprojects)))[0][0]

        #This was moved down because creating sections requires a project id
        defaultsection = Section(f"_{self.name}", self)
        self.sections.append(defaultsection)

    def set_name(self, name):                 #Set name of project
        self.name = name

        # Update name of project in projects table
        ExecuteCommand("UPDATE projects set title = ? where id = ?", (name, self.id))
        
    def set_color(self, color):
        self.color = color

        # Update color of project in projects table
        ExecuteCommand("UPDATE projects set color = ? where id = ?", (color, self.id))
        
    def add_section(self, newsection):
        self.sections.append(newsection)

        # Update sectioncount in projects table
        ExecuteCommand("UPDATE projects set sectioncount = ? where id = ?", (len(self.sections), self.id))
        
    def remove_section(self, delsection):
        self.sections.remove(delsection)

        # Update sectioncount in projects table
        ExecuteCommand("UPDATE projects set sectioncount = ? where id = ?", (len(self.sections), self.id))

    def add_project(self, newproject):
        self.subprojects.append(newproject)

        # Update projectcount in projects table
        ExecuteCommand("UPDATE projects set projectcount = ? where id = ?", (len(self.subprojects), self.id))

    def remove_project(self, delproject):
        self.subprojects.remove(delproject)
        
        # Update projectcount in projects table
        ExecuteCommand("UPDATE projects set projectcount = ? where id = ?", (len(self.subprojects), self.id))

    def add_parentproject(self, newparent):
        self.parentprojects.append(newparent)

    def remove_parentproject(self, delparent):
        self.parentprojects.remove(delparent)

    def display_sections(self):
        print(*self.sections,sep='\n')

    def display_projects(self):
        print(*self.subprojects,sep='\n')

    def display_parentprojects(self):
        print(*self.parentprojects,sep='\n')
          

    def __str__(self):
        return  f'Project name: {self.name} \
                \nDisplay color: {self.color} \
                \nSections: {[str(s) for s in self.sections]}'

    def __repr__(self):
        return f"Project({self.name},{self.color},{self.sections},{self.subprojects},{self.parentprojects})"

class task:

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


    def __str__(self):
        return f"""Task with priority {str(self.priority)} \n Due on {self.DueDate}"""

    def __repr__(self):                         
        return f"task('{self.TaskTitle}','{self.TaskDesc}',{self.priority.PriorityLevel},{self.DueDate},{self.Labels})" 
        #Repr returns how to create the task
