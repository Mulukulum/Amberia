#Required imports
#Importing all the log functions
from Codebase.ErrorLogs.logging import ErrorLog,Log,DBLog,DBOnlyLog

#Importing functions to interface with the database
from Codebase.Functions.Database import ExecuteCommand,ExecuteScript            

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

    def set_project(self, newproject):   #Set the project to which the section belongs
        self.project = newproject         

    def add_task(self, newtask):         #Add a new task to the section
        self.tasks.append(newtask)

    def remove_task(self, deltask):      #Remove a task from the list of tasks
        self.tasks.remove(deltask)

    def display_tasks(self):             #Display the list of tasks
        print(*self.tasks,sep='\n')      #Displays tasks without a for loop         

    def __repr__(self):
        return f"Section({self.name},{self.project},{self.tasks})"              

    def __str__(self):
        return f'Section name: {self.name} \nProject name: {self.project.name} \nTasks: {[str(t) for t in self.tasks]}'        
        #fstring returns the string representation


class Task:
    def _init_(self, prio, date, time=None, labels=None, tasks=None, notes=None):
        self.priority = prio
        self.duedate = date
        self.duetime = time
        self.labels = labels
        self.notes = notes
        self.tasks = tasks

    def _str_(self):
        return 'Task with priority ' + str(self.priority) + '\n'\
                'Due on ' + self.duedate



class Section:
    cur_section_id = 1

    def _init_(self, name, project=None, tasks=[]):
        self.id = Section.cur_section_id
        Section.cur_section_id += 1

        self.name = name                 #Initialize name of section
        self.project = project
        self.tasks = tasks               #Initialize a list of tasks
        
        # Add new section to sections table
        ExecuteCommand("INSERT INTO sections (sectionid, title, taskcount, parentprojectid) VALUES (?, ?, ?, ?);",
                       (self.id, self.name, len(self.tasks), project.id if project != None else 0))

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
        for t in self.tasks:
            print(t)

    def _repr_(self):
        return f"Section({self.name},{self.project},{self.tasks})"

    def _str_(self):
        return 'Section name: ' + self.name + '\nProject name: ' + self.project.name + \
               '\nTasks: ' + str([str(t) for t in self.tasks])


class Project:
    cur_proj_id = 1
    
    def _init_(self, name, color, projects = [], parentprojects = []):
        self.id = Project.cur_proj_id
        Project.cur_proj_id += 1
        self.name = name                 #Initialize name of project
        self.color = color               #Initialize display color
        self.sections = []               #Initialize list of sections
        defaultsection = Section(f"_{self.name}", self)
        self.sections.append(defaultsection)
        self.subprojects = projects           #Initialize list of sub projects 
        self.parentprojects = parentprojects  #Initialize list of parent projects
        
        # Add new project to projects table
        ExecuteCommand("INSERT INTO projects (id, title, color, sectioncount, projectcount) VALUES (?, ?, ?, ?, ?);",
                       (self.id, self.name, self.color, len(self.sections), len(self.subprojects)))

    def set_name(self, name):                 #Set name of project
        self.name = name

        # Update name of project in projects table
        ExecuteCommand("UPDATE projects set title = ? where id = ?", (name, self.id));
        
    def set_color(self, color):
        self.color = color

        # Update color of project in projects table
        ExecuteCommand("UPDATE projects set color = ? where id = ?", (color, self.id));
        
    def add_section(self, newsection):
        self.sections.append(newsection)

        # Update sectioncount in projects table
        ExecuteCommand("UPDATE projects set sectioncount = ? where id = ?", (len(self.sections), self.id));
        
    def remove_section(self, delsection):
        self.sections.remove(delsection)

        # Update sectioncount in projects table
        ExecuteCommand("UPDATE projects set sectioncount = ? where id = ?", (len(self.sections), self.id));

    def add_project(self, newproject):
        self.subprojects.append(newproject)

        # Update projectcount in projects table
        ExecuteCommand("UPDATE projects set projectcount = ? where id = ?", (len(self.subprojects), self.id));

    def remove_project(self, delproject):
        self.subprojects.remove(delproject)
        
        # Update projectcount in projects table
        ExecuteCommand("UPDATE projects set projectcount = ? where id = ?", (len(self.subprojects), self.id));

    def add_parentproject(self, newparent):
        self.parentprojects.append(newparent)

    def remove_parentproject(self, delparent):
        self.parentprojects.remove(delparent)

    def display_sections(self):
        for s in self.sections:
            print(s)

    def display_projects(self):
        for p in self.subprojects:
            print(p)

    def display_parentprojects(self):
        for p in self.parentprojects:
            print(p)

    def _str_(self):
        return 'Project name: ' + self.name + \
               'Display color: ' + self.color + \
               'Sections: ' + str([str(s) for s in self.sections])

    def _repr_(self):
        return f"Project({self.name},{self.color},{self.sections},{self.subprojects},{self.parentprojects})"

class task:
    def __init__(self, TaskTitle, TaskDesc=None, priority=None, DueDate=None, Labels=None): #Initializes the class
        self.TaskTitle=TaskTitle
        self.TaskDesc=TaskDesc
        self.DueDate=DueDate
        if Priority.IsValidPriority(priority):          #Checks if the incoming argument is a valid priority level
            self.priority=Priority(priority)            #If so, then give the task its priority
        else:
            self.priority=Priority(10)                  #If not, then set it to a default value of 10
            Log(f"Task {self.TaskTitle} given no priority. Default Value Assigned")

        if Labels==None:                                #Checks if any labels are selected
            self.Labels=[]                              #Makes it an empty list instead of None
        else: 
            self.Labels=Labels                          #Makes a list of the selected labels

    def set_label(self,NewLabel):
        if NewLabel in self.Labels:                     #Checks if the label is already selected
            self.Labels.remove(NewLabel)                #Removes the label if it is already selected
        else: 
            self.Labels.append(NewLabel)                #Adds the label if it isnt selected

    def __repr__(self):                         
        return f"task('{self.TaskTitle}','{self.TaskDesc}',{self.priority},{self.DueDate},{self.Labels})" 
        #Repr returns how to create the task
