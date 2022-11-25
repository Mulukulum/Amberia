
#This file contains the functions to take stored values from the DB and convert that into python objects

from Codebase.Functions.Database import ExecuteCommand

from Codebase.Classes import classes as cl

#Create the Projects
def AddProjects():

    Projects=ExecuteCommand(f"SELECT project_id,project_title,project_color,project_sectioncount FROM projects")
    
    for Project in Projects:

        ...





