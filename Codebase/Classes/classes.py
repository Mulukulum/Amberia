#Required imports
#Importing all the log functions
from Codebase.ErrorLogs.logging import ErrorLog,Log

#Importing functions to interface with the database
from Codebase.Functions.Database import ExecuteCommand,ExecuteScript            

#Importing The Required Colors for Labels
from Codebase.Functions.Colors import GetRandomColor

#Importing notification fnctions
from plyer import notification

from os.path import dirname
PathOfCodebase=dirname(dirname(__file__))

import threading

import sys,time

import datetime

class Project:
    
    #Empty dictionary to store the instances of all the projects
    Instances=dict()

    def __init__(self, ProjectTitle: str, ProjectColor: int=678452056,LoadedFromDB: bool=False,ID: int=-1,DefaultSectionID: int=-1):
        #Initialize name of project
        self.Title = ProjectTitle            
        #Set a random color if No Color was specified or the Color is Invalid
        if ProjectColor>=16777215:
            self.Color=GetRandomColor()
        else:
            self.Color=ProjectColor
        #Sets the ID of the project
        self.ID=ID
        #Add the Project to the Database
        if LoadedFromDB==False: self.ID=ExecuteCommand(
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
        self.Sections=dict()
        #Create and Set the DefaultSection
        self.DefaultSection = Section(SectionProject=self , SectionTitle=f"_{self.Title}",IsDefaultSection=True,LoadedFromDB=LoadedFromDB,ID=DefaultSectionID)

    def DeleteProject(self):
        #Remove all Sections from the Project
        self.RemoveAllSections()
        ExecuteCommand(f"DELETE FROM projects WHERE project_id=?",(self.ID,))
        Project.Instances.pop(self.ID)

    def RemoveAllSections(self):
        #Uses a while loop to clear the dictionary
        while self.Sections!={}:
            self.Sections.popitem()[-1].DeleteSection()

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
        Section(SectionProject=self,SectionTitle=SectionTitle)
        #Update the sectioncount attribute
        ExecuteCommand("UPDATE projects SET project_sectioncount=project_sectioncount+1 WHERE project_id=?",(self.ID,))

    def RemoveSection(self, SectionID: int):
        if SectionID not in self.Sections:
            if SectionID not in Section.Instances:
                return ErrorLog("WARNING: Section Delete Request Issued for Non-Existent Section")
            return ErrorLog("WARNING: Section Delete Request Issued for Invalid Section")
        self.Sections[SectionID].DeleteSection()

    def __str__(self):
        return  f"""
        Project Title : {self.Title}
        Color : {self.Color}
        {self.ID=}
        Section Count: {len(self.Sections)}
        List of Sections:
            {[s.Title for s in list(self.Sections.values())]}
        """

class Section:
    
    #Dictionary to store the instances of all available Section objects
    Instances=dict()

    def __init__(self,SectionProject: Project, SectionTitle: str, IsDefaultSection=False,LoadedFromDB: bool=False,ID: int=-1):

        #Check Validity of The section Title
        #Ensuring that SectionTitle's can't start with a single underscore followed by characters
        if IsDefaultSection==True :
            self.Title=SectionTitle
        else:
            if SectionTitle==f"_{SectionProject.Title}":    #If the section title's name is the same as the default section
                self.Title=(f"_{SectionTitle}")   #Sets Title to __sectionname
            else:
                self.Title=SectionTitle
        self.IsDefaultSection=IsDefaultSection
        self.ParentProject = SectionProject    #Get the Parent Project
        self.Tasks=dict()                   #Set the dict of Tasks (TaskId:TaskObject)
        self.ActiveTasks=dict()            #Set the dict with incomplete tasks (unused feature)
        self.TextTasks=dict()              #Unused feature               

        self.ID=ID
        #Add the Section to the Database
        if LoadedFromDB==False: self.ID=ExecuteCommand(
        """
        INSERT INTO sections
        (section_parentprojectid,
        section_title,
        section_taskcount,
        section_activetaskcount,
        section_texttaskcount
        )
        VALUES (?,?,?,?,?)
        RETURNING section_id
        """,
        (self.ParentProject.ID, #ID of the parentProject
        self.Title,       #Title of the Section
        0,0,0                 #New section so no tasks added
        ))[0][0]             
        #Add the section to the dictionary of instances
        Section.Instances[self.ID]=self
        #Add the Section to the dictionary of Sections in the Project
        self.ParentProject.Sections[self.ID]=self

    def DeleteSection(self):

        #Remove all the Tasks 
        self.DeleteAllTasks()
        #Remove reference from project
        self.ParentProject.Sections.pop(self.ID,None)

        #Decrement project_sectioncount from database
        ExecuteCommand("UPDATE projects SET project_sectioncount=project_sectioncount-1 WHERE project_id=?",(self.ParentProject.ID,))
        #Remove section from the Database
        ExecuteCommand("DELETE FROM sections WHERE section_id=?",(self.ID,)) 

    def AddTask(self, Title: str, Description: str, Priority: int, DueDate:datetime.datetime=None,Labels: list=None):         #Add a new task to the section        
        Task(ParentSection=self, TaskTitle=Title, TaskDesc=Description, PriorityLevel=Priority, DueDate=DueDate, labels=Labels)

    def DeleteAllTasks(self):
        #Clears the Dictionary with active tasks
        #self.ActiveTasks.clear()
        #While the section still has tasks
        while self.Tasks!={}:
            #Pop and delete them one after another
            self.Tasks.popitem()[-1].DeleteTask()          
          
    def __str__(self):
        #fstring returns the string representation
        return f"""
        Title : {self.Title}
        Project : {self.ParentProject.Title}
        {self.ID=}
        {self.ParentProject.ID=}
        Task Count : {len(self.Tasks)}
        """
        #Task Active : {len(self.ActiveTasks)}

class Label:

    CreationSucess=True
    LabelInstances={}
    LabelNames=[]

    #Class initialisation | Method returns True if Creation was successful
    def __init__(self, Title : str ,Color : int=None,LoadedFromDB: bool=False,ID: int=-1) -> None:

        if Label.LabelExists(Title):
            #If the Label already exists, then Log an Error
            ErrorLog(f" TRIVIAL : Attempt to create label with name {Title} which already exists")
            Label.CreationSucess=False
        
        else:
            self.Title=Title                #Set Title
            self.Tasks=[]
            self.Widgets=[]                 #Sets the list with Appropriate QWidgets 
            if Color==None:                 #If there is no Color specified 
                self.Color=GetRandomColor() #Pick a random Color

            else:
                #Set the specified Color
                self.Color=Color
            
            self.ID=ID
            if LoadedFromDB==False: 
                self.ID=ExecuteCommand("INSERT INTO labels(label_title,label_color,label_taskcount) VALUES(?,?,0) RETURNING label_id;",(self.Title,self.Color))
            
            #Dictionary with LabelID<int> : LabelObject
            Label.LabelInstances[self.ID]=self
            #Add the name to the list of LabelNames
            Label.LabelNames.append(self.Title)
            #Set the flag to True
            Label.CreationSucess=True

    def DeleteLabel(self,LabelID: int):
        
        if LabelID in Label.LabelInstances :
            
            #Decouples the Label from all tasks
            self.DeLinkFromTasks()            
            for LabelWidget in self.Widgets:
                #Deletes all instances of this widget
                LabelWidget.deleteLater()
            self.Widgets.clear()
            #Remove any references to the label
            Label.LabelInstances.pop(LabelID)
            Label.LabelNames.remove(self.Title)
            ExecuteCommand("DELETE FROM labels WHERE label_id=?",(LabelID,))
    
    def DeLinkFromTasks(self):
        while self.Tasks!=[]:
                Task.Instances[self.Tasks[0]].RemoveLabel(self.ID)

    @classmethod
    def ValidRename(cls,LabelTitle: str) -> bool:
        return not Label.LabelExists(LabelTitle)

    @classmethod
    def LabelExists(cls,LabelTitle: str) -> bool:
        #Check whether the label is currently active
        if LabelTitle in Label.LabelNames:
            return True
        else:
            return False

    #Method to change the color of a label
    def SetColor(self,Color: int) -> None :

        if Color<=16777215:
            self.Color=Color

        else:
            ErrorLog(f" TRIVIAL : NO-OP DUE TO Invalid Color Assignment ({Color}) for Label {self.Title}")

    #Use this method only when rename availability is known
    def RenameLabel(self,NewName: str):
        
        #Change the Database
        ExecuteCommand("UPDATE labels SET label_title=? WHERE label_id=?",(NewName,self.ID))
        ExecuteCommand("UPDATE labelsfortasks SET label=? WHERE label=?",(NewName,self.ID))
        #Update the python stuff
        Label.LabelNames.remove(self.Title)
        Label.LabelNames.append(NewName)
        #Update the object in python
        self.Title=NewName

    def RandomizeColor(self) -> None:
        self.Color=GetRandomColor()

    #Label repr 
    def __repr__(self) -> str:
        return f'Label({self.Title},{self.Color},{self.ID})'
    
    #String Representation
    def __str__(self) -> str:
        return f'Label {self.Title} Color {self.Color} ID {self.ID}'

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
        1:10820909,
        2:12994048,
        3:9526818,
        4:5865301,
        5:5278230,
        6:878910,
        7:1209197,
        8:804465,
        9:4393866,
        10:7605130,
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
        ExecuteScript(ScriptSetDefaultColors)           #Runs the script to set the default colors
        ColorCache=DefaultPriorityColors.copy()         #Updates the Cache
    ColorCache.update(Resultant)
    del Resultant                                       #Deletes the resultant list because its not needed

    #Class method that ensures priority level call is valid    
    @classmethod
    def IsValid(cls,PrLevel: int) -> bool:      
        if PrLevel in cls.ValidPriorites: return True
        else: return False

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
    def __init__(self, 
    ParentSection: Section, TaskTitle: str, TaskDesc: str=None, 
    PriorityLevel: int=Priority.UpperBound, ReminderState: int=0, 
    DueDate: datetime.datetime=None, CompletionDate: datetime.datetime=None,
    labels: list=None, CompletionState: int=0,
    LoadedFromDB: bool=False, ID: int=-1): #Initializes the class

        #Sets the Title and Description for the task
        self.TaskTitle=TaskTitle
        self.TaskDesc=TaskDesc
        self.ParentSection=ParentSection
        self.ShowReminder=ReminderState
        if labels==None:
            labels=[]
        self.DueDate=DueDate
        self.Completed=CompletionState                              #sets completed to False, sql doesn't have bool so I'm using 0 and 1
        self.CompletedDate=CompletionDate                                      #makes the object for completed date

        #Priority Level of Task
        if Priority.IsValid(PriorityLevel):          #Checks if the incoming argument is a valid priority level
            self.PriorityLevel=PriorityLevel         #If so, then give the task its priority level
        else:
            self.PriorityLevel=Priority.UpperBound   #If not, then set it to a default upperbound value
            ErrorLog(f"Task {self.TaskTitle} given no priority. Default Value {self.PriorityLevel} Assigned")

        self.Color=Priority.ColorOfLevel(PriorityLevel)     #And assign the color as well
        self.ReminderThread=NotificationThread(self)        #Assign the thread class
        #ID of Task
        self.ID=ID
        if LoadedFromDB==False: self.ID=ExecuteCommand(f"""
        INSERT INTO tasks(
        task_title,
        task_description,
        task_projectid,
        task_sectionid,
        task_priority,
        task_completed,
        task_duedate,
        task_showreminder
        ) VALUES(?,?,?,?,?,?,?,?)
        RETURNING task_id;
        """,
        (self.TaskTitle,
        self.TaskDesc,
        ParentSection.ParentProject.ID,
        ParentSection.ID,
        self.PriorityLevel,
        self.Completed,
        self.DueDate,
        self.ShowReminder,
        )
        )[0][0]
        #Add the task to the dictionary of instances
        Task.Instances[self.ID]=self
        #Add a reference to this task in sections
        self.ParentSection.Tasks[self.ID]=self
        #self.ParentSection.ActiveTasks[self.ID]=self
        if LoadedFromDB==False: 
            ExecuteCommand("UPDATE sections SET section_taskcount=section_taskcount+1,section_activetaskcount=section_activetaskcount+1 WHERE section_id=?",(self.ParentSection.ID,))

        #Makes the List of labels assigned to the task
        if LoadedFromDB==False:
            self.Labels=[]  # list <int>
            #Note that Label is an int, and Labels is a list of ints
            for labelId in labels:
                self.AddLabel(labelId)
        
        else:
            #For Loading Labels Directly from the Database, we have to ensure that the label object exists first
            self.Labels=[]
            for labelId in labels:
                self.Labels.append(labelId)
        
        if DueDate!=None:
            self.ReminderThread.ScheduleReminder(DueDate)


    def ToggleLabel(self,Label: int):
        if Label in self.Labels:
            #Remove the label from the task
            self.RemoveLabel(LabelID=Label)
        else:
            #Add the Label to the task
            self.AddLabel(Label)

    def AddLabel(self,NewLabelID: int):

        Label.LabelInstances[NewLabelID].Tasks.append(self.ID)
        #Insert into the Labels for tasks table
        ExecuteCommand("INSERT INTO labelsfortasks(task,label) VALUES(?,?);",(self.ID,NewLabelID))
        #Increment the TaskCount
        ExecuteCommand("UPDATE labels SET label_taskcount=label_taskcount+1 WHERE label_id=?;",(NewLabelID,))
        self.Labels.append(NewLabelID)

    def RemoveAllLabels(self):
        while self.Labels!=[]:
            self.RemoveLabel(self.Labels[0])

    def RemoveLabel(self,LabelID: int):
        
        #Delete from the Labels for tasks table
        ExecuteCommand("DELETE FROM labelsfortasks WHERE label=? AND task=?;",(LabelID,self.ID))

        #Decrement the TaskCount
        ExecuteCommand("UPDATE labels SET label_taskcount=label_taskcount-1 WHERE label_id=?;",(LabelID,))

        #From the label object's list of Task IDs, remove this task
        Label.LabelInstances[LabelID].Tasks.remove(self.ID)
        self.Labels.remove(LabelID)

    def ReConfigureTask(self, TaskTitle: str=None, TaskDesc: str=None, PriorityLevel: int=None, Reminder: int=None, DueDate: datetime.datetime=None, Labels: list=None,Remindertitle=None,Remindermsg=None,ClearDueDate: bool=False):
        if TaskTitle!=None:
            self.TaskTitle=TaskTitle                    #Changes the title to a newly provided title, if not provided stays the same
        if TaskDesc!=None:
            self.TaskDesc=TaskDesc                      #Changes the desc to a newly provided desc
        if DueDate!=None:
            if ClearDueDate:
                self.DueDate=None
            else:
                self.DueDate=DueDate                        #Changes the due date to a newly provided due date
        if Reminder==None:
            Reminder=0
        else:        
            if Reminder: 
                Reminder=1      
                self.ReminderThread.ScheduleReminder(self.DueDate,Remindertitle,Remindermsg)
            else:
                Reminder=0
                self.ReminderThread.StopCurrentThread()
        
        
        if Priority.IsValid(PriorityLevel):          #Checks if the incoming argument is a valid priority level
            self.PriorityLevel=PriorityLevel            #If so, then give the task its new priority

        if Labels!=None:
            self.Labels=[]
            for Label in Labels:
                self.AddLabel(Label)
        else:
            self.Labels=[]
        
        ExecuteCommand(f"""
        UPDATE tasks SET task_title=?,task_description=?,task_priority=?, 
        task_duedate=?,task_showreminder=? WHERE task_id=?""",(
            self.TaskTitle,
            self.TaskDesc,
            self.PriorityLevel,
            self.DueDate,
            self.ShowReminder,
            self.ID
            ))

    def UpdateTaskDesc(self,Desc):
        self.TaskDesc=Desc
        ExecuteCommand("""UPDATE tasks SET task_description=? WHERE task_id=?""",(self.TaskDesc,self.ID))

    def CompleteTask(self):
        self.Completed=1                                #Completes the task
        self.CompletedDate=datetime.datetime.now()      #records the completed time
        #self.ParentSection.ActiveTasks.pop(self.ID)
        ExecuteCommand(f"UPDATE tasks SET task_completed=?, task_completed_date=? WHERE task_id=?",(1,self.CompletedDate,self.ID))
        ExecuteCommand(f"UPDATE sections SET section_activetaskcount=section_activetaskcount-1 WHERE section_id=?",(self.ParentSection.ID,))
        self.ReminderThread.StopCurrentThread()

    def DeleteTask(self):
        self.ReminderThread.StopCurrentThread()
        #Remove all the labels
        self.RemoveAllLabels()
        ExecuteCommand("UPDATE sections SET section_taskcount=section_taskcount-1 WHERE section_id=?",(self.ParentSection.ID,))
        ExecuteCommand(f"DELETE FROM tasks WHERE task_id=?;",(self.ID,))
        #Pops the task from its parent section
        self.ParentSection.Tasks.pop(self.ID,None)
        #Pops the item from the dictionary of instances
        Task.Instances.pop(self.ID)

    def SetReminderState(self,State:int,Title=None,msg=None):
        if Title==None:
            if len(self.TaskTitle)>20:
                Title=f"{self.TaskTitle[0:20]}... is Due Today"
            else:
                Title=f"{self.TaskTitle} is Due Today"
        if msg==None:
            TaskDesc="" if self.TaskDesc==None else self.TaskDesc
            msg=f"Priority {int(self.PriorityLevel)} in {self.ParentSection.ParentProject.Title[0:20]}\n {TaskDesc[0:31]}"
        self.ShowReminder=State
        ExecuteCommand("UPDATE tasks SET task_showreminder=? WHERE task_id=?",(self.ShowReminder,self.ID))
        #If reminder is to be set
        if State:
            self.ReminderThread.StopCurrentThread()
            self.ReminderThread=NotificationThread(self)
            self.ReminderThread.ScheduleReminder(self.DueDate,Title,msg)
        else: 
            self.ReminderThread.StopCurrentThread()
            
    def ChageDueDate(self, NewDueDate: datetime.datetime):
        self.DueDate=NewDueDate                         #Accepts a new due date
        ExecuteCommand(f"UPDATE tasks SET task_duedate=? WHERE task_id=?",(NewDueDate,self.ID))
        if self.ShowReminder:
            #Sets the prev thread to stop
            self.ReminderThread.StopCurrentThread()
            self.ReminderThread=NotificationThread(self)
            self.ReminderThread.ScheduleReminder(NewDue=NewDueDate)
    
    #Update the PriorityLevel of the Task
    def UpdatePriority(self, priority: int):
        if Priority.IsValid(priority):                      #Checks if the incoming argument is a valid priority level
            self.PriorityLevel=Priority(priority)           #If so, then give the task its new priority
            self.Color=Priority.ColorOfLevel(priority)      #Give the task its new color
            ExecuteCommand(f"UPDATE tasks SET task_priority=? WHERE task_id=?",(self.PriorityLevel,self.ID))
        else:
            ErrorLog(f"WARNING : NO-OP DUE TO Invalid Argument for Priority : {priority}")

    @classmethod
    def Notify(cls, Title: str, Message: str):
        notification.notify(
            title=Title,
            message=Message,
            app_name='Amberia',
            app_icon=PathOfCodebase+r'//GUI//UI_Files//AppIcon.ico',
            timeout=5
            )

class TextTask:
        
    @classmethod
    def Notify(cls, Title: str, Message: str):
        notification.notify(
            title=Title,
            message=Message,
            app_name='Amberia',
            app_icon=PathOfCodebase+r'//GUI//UI_Files//AppIcon.ico',
            timeout=5
            )
    
    Instances=dict()
    
    def __init__(self,ParentSection: Section , TaskText: str,LoadedFromDB: bool=False,ID: int=-1) -> None:
        self.TaskText=TaskText
        self.ParentSection=ParentSection
        self.ParentProject=ParentSection.ParentProject

        self.ID=ID
        if LoadedFromDB: self.ID=ExecuteCommand(f"""
        INSERT INTO texttask(texttask_text,texttask_sectionid,texttask_projectid)
        VALUES (?,?,?) RETURNING texttask_id;
        """,(self.TaskText,self.ParentSection.ID))[0][0]

        self.ParentSection.TextTasks[self.ID]=self
        ExecuteCommand(f"UPDATE sections SET section_texttaskcount=section_texttaskcount+1 WHERE section_id=?",(self.ParentSection.ID,))
        TextTask.Instances[self.ID]=self
    
    def DeleteTextTask(self):
        #Remove the TextTask from the Section and Instances dict
        self.ParentSection.TextTasks.pop(self.ID)
        TextTask.Instances.pop(self.ID)
        ExecuteCommand("UPDATE sections SET section_texttaskcount=section_texttaskcount-1 WHERE section_id=?",(self.ParentSection.ID,))
        ExecuteCommand(f"DELETE FROM texttasks WHERE task_id=?;",(self.ID,))

    def UpdateText(self,NewText: str):
        self.TaskText=NewText
        ExecuteCommand("UPDATE texttasks SET texttask_text=? WHERE texttask_id=? ;",(self.TaskText,self.ID))


class TaskBuilder:

    def __init__(self,IsTextTask: bool, TaskTitles: list, TaskDescs: list=None,ParentSection: Section=None, PriorityLevel: int=None, DueDate: datetime.datetime=None, Labels: list=list()):
        
        if Priority.IsValid(PriorityLevel):
            pass
        else:
            PriorityLevel=Priority.UpperBound

        if IsTextTask:
            for Text in TaskTitles:
                TextTask(ParentSection=ParentSection,TaskText=Text)
        else:
            for Title,Descs in zip(TaskTitles,TaskDescs):
                Task(ParentSection=ParentSection,TaskTitle=Title,TaskDesc=Descs,PriorityLevel=PriorityLevel,DueDate=DueDate,labels=Labels)
    

#Class for sending notifs using threads
class NotificationThread:

    def __init__(self,Task: Task) -> None:
        self.Task=Task
        self.StopFlag=threading.Event()
        self.StopFlag.clear()

    def StopCurrentThread(self):
        #Sets the stop flag
        self.StopFlag.set()
        
    def ScheduleReminder(self,NewDue: datetime.datetime,Title=None,Message=None):
        #If stop is set, then show the reminder
        if self.StopFlag.is_set():
            self._ShowReminder(NewDue,Title,Message)
        else:
            self.StopCurrentThread()
            self._ShowReminder(NewDue,Title,Message)
    
    def _ShowReminder(self,Date: datetime.datetime,title=None,msg=None):
        #If the date is less than the current time then just return
        self.StopFlag.clear()
        now=datetime.datetime.now()
        if Date==None:
            return
        if now+datetime.timedelta(0,3) >= Date:
            return
        #if title==None: self.title=f"Task {self.Task.TaskTitle[0:20]}... is due"
        #if msg==None : self.msg=f"Priority {self.Task.PriorityLevel} in Project {self.Task.ParentSection.ParentProject.Title[0:20]}..."
        self.timediff=Date-datetime.datetime.now()
        #Create a daemon thread
        self.CurrentThread=threading.Thread(target=self.ThreadFunction,args=(self.timediff.total_seconds(),title,msg),daemon=True)
        #Starts the thread
        self.CurrentThread.start()
    

    def ThreadFunction(self,delta: float,title,msg):
        TimeConst=0.5
        #Calculate the number of iterations to perform
        iterations=delta//TimeConst 
        final=delta%TimeConst
        #While the stop flag is not set and the time has not been reached
        while self.StopFlag.is_set()==False and iterations:
            time.sleep(TimeConst)
            iterations-=1
        #If the stop flag is set, then return immediately
        if self.StopFlag.is_set():
            return
        time.sleep(final)
        #Task Notifications 
        self.Task.Notify(Title=title,Message=msg)
            
            
