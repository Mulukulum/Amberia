import datetime
import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Codebase.Classes import classes as cl
from Codebase.GUI.UI_Classes.AmberMainWin import AmberWindowUI
from Codebase.GUI.UI_Classes.TasksTodayWindow import TaskTodayUI
from Codebase.GUI.UI_Classes.TaskWidget import TaskWidgetUI


class TodayTasksWidget(QtWidgets.QWidget):

    def __init__(self,frame) -> None:
        super().__init__(frame)
        self.ui=TaskTodayUI()
        self.ui.setupUi(self)
        #Sets the name of the widget
        self.setObjectName(u"TaskTodayWidget")
    
    def AddTaskToWidget(self,TaskObject: cl.Task):
        
        ...

class TaskWidget(QtWidgets.QWidget):

    def __init__(self,frame) -> None:
        super().__init__(frame)
        self.ui=TaskWidgetUI()
        self.ui.setupUi(frame)
    
    def SetInformation(self,TaskObject: cl.Task):
        
        #Sets the Display to show priority Level
        self.ui.PriorityLevelDisplay.display(TaskObject.PriorityLevel)

        #Sets the Description to the Description of the Task
        if TaskObject.TaskDesc!=None:
            self.ui.TaskDescription.setText(TaskObject.TaskDesc)
        else:
            self.ui.TaskDescription.setPlaceholderText(u'Enter Description Here')
        
        #Get the Title of the Task
        Title=TaskObject.TaskTitle

        #If the task is given a duedate
        if TaskObject.DueDate==None:
            self.ui.DaysLeftDisplay.hide()
            self.ui.DaysLeftLabel.hide()
