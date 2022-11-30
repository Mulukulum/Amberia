
#This file contains the functions to take stored values from the DB and convert that into python objects

from Codebase.Functions.Database import ExecuteCommand

from Codebase.Classes import classes as cl

#Create the Projects
def AddProjects():

    Projects=ExecuteCommand("SELECT project_id,project_title,project_color,project_sectioncount FROM projects")
    
    for Project in Projects:
        proj_id=Project[0]
        project_title=Project[1]
        project_color=Project[2]
        default_section_id=ExecuteCommand("SELECT section_id FROM sections WHERE section_parentprojectid=?",(proj_id,))[0][0]
        #This happens when the project doesn't have a default section setup
        cl.Project(ProjectTitle=project_title,ProjectColor=project_color,LoadedFromDB=True,ID=proj_id,DefaultSectionID=default_section_id)
    #Projects Added

def AddLabels():

    Labels=ExecuteCommand("SELECT label_id,label_title,label_color FROM labels")
    for Label in Labels:
        label_id=Label[0]
        label_title=Label[1]
        label_color=Label[2]
        cl.Label(Title=label_title,Color=label_color,ID=label_id,LoadedFromDB=True)

def AddSections():

    Sections=ExecuteCommand("SELECT section_id,section_parentprojectid,section_title FROM sections")
    for Section in Sections:
        id=Section[0]
        projectid=Section[1]
        title=Section[2]
        if title.startswith("_"): continue
        cl.Section(
            SectionProject=cl.Project.Instances[projectid],
            SectionTitle=title,
            LoadedFromDB=True,
            ID=id
        )

def AddTasks():

    Tasks=ExecuteCommand("""
    SELECT task_id,task_title,task_description,task_projectid,
    task_sectionid,task_priority,task_completed,task_duedate,task_completed_date FROM tasks
    """)

    for Task in Tasks:
        id=Tasks[0]
        title=Tasks[1]
        desc=Tasks[2]
        # projectid=Tasks[3]
        sectionid=Tasks[4]
        prlevel=Tasks[5]
        completionstate=Tasks[6]
        duedate=Tasks[7]
        completeddate=Tasks[8]
        cl.Task(
            ParentSection=cl.Section.Instances[sectionid],
            TaskTitle=title,
            TaskDesc=desc,
            PriorityLevel=prlevel,
            DueDate=duedate,
            LoadedFromDB=True,
            CompletionState=completionstate,
            CompletionDate=completeddate,
            ID=id
            )

def AddTextTasks():

    TextTasks=ExecuteCommand("SELECT texttask_id,texttask_text,texttask_sectionid FROM texttasks")
    for Texttask in TextTasks:
        id=Texttask[0]
        txt=Texttask[1]
        sectionid=Texttask[2]
        cl.TextTask(
            ParentSection=cl.Section.Instances[sectionid],
            TaskText=txt,
            LoadedFromDB=True,
            ID=id
        )

def Retrieve():
    #Labels goes first
    AddLabels()
    AddProjects()
    AddSections()
    AddTasks()
    AddTextTasks()

Retrieve()



