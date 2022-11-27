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

    #Lambda Function because python somehow doesn't have a method for this
    OrdinalTimeFunction=lambda n : str(n) + {1:'st',2:'nd',3:'rd'}.get(abs(n)%10,'th')

    def __init__(self,frame) -> None:
        super().__init__(frame)
        self.ui=TaskWidgetUI()
        self.ui.setupUi(frame)
    
    def SetInformation(self,TaskObject: cl.Task):
        
        #Sets the name of the object for easy identification
        self.setObjectName(f"TaskWidget{TaskObject.ID}")
        
        #Sets the Display to show priority Level
        self.ui.PriorityLevelDisplay.display(TaskObject.PriorityLevel)

        #Sets the Description to the Description of the Task
        if TaskObject.TaskDesc!=None:
            self.ui.TaskDescription.setText(TaskObject.TaskDesc)
        else:
            self.ui.TaskDescription.setPlaceholderText(u'Enter Description Here')
        
        #Get the Title of the Task
        Title=TaskObject.TaskTitle
        Due=TaskObject.DueDate
        Completed=TaskObject.Completed

        #If the task is given a duedate
        if Due==None:

            #Then Hide the days left part
            self.ui.DaysLeftDisplay.hide()
            self.ui.DaysLeftLabel.hide()
            Text=Title
        
        else:
            if not Completed:
                Text=f"Due On {Due.strftime(f'%a, {TaskWidget.OrdinalTimeFunction(Due.day)} %b %Y')} "+Title
                
            else:
                Text=f"Task Finished at {TaskObject.CompletedDate.strftime('%c')}"

                #We can hide these labels since there's no need for a days left counter
                self.ui.DaysLeftDisplay.hide()
                self.ui.DaysLeftLabel.hide()
        
        #Set the Title text
        self.ui.TaskTitle_label.setText(Text)

        #Show the labels if they're meant to be shown
        if 1:
            self.ui.DaysLeftDisplay.show()
            self.ui.DaysLeftLabel.show()


        
        
