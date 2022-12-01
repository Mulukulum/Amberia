import datetime
import sys
import os
import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
path=os.path.dirname(__file__)+r'\\StyleSheet\\Amberia.qss'
with open(path) as f:
    StyleSheet=f.read()
from Codebase.Classes import classes as cl
from Codebase.GUI.UI_Classes.TasksTodayWindow import TaskTodayUI
from Codebase.GUI.UI_Classes.TaskWidget import TaskWidgetUI
from Codebase.GUI.UI_Classes.LabelEditor import LabelWidgetUI
from Codebase.GUI.UI_Classes.ProjectWidget import ProjectWidgetUI
from Codebase.GUI.UI_Classes.SectionWidget import SectionWidgetUI
from Codebase.GUI.UI_Classes.TaskEdit import TaskEditUI
from Codebase.Functions.Database import ExecuteCommand
from Codebase.ErrorLogs.logging import ErrorLog
from Codebase.Functions.Colors import HexFormat

class TodayTasksWidget(QtWidgets.QWidget):

    def __init__(self,frame) -> None:
        super().__init__(frame)
        self.ui=TaskTodayUI()
        self.ui.setupUi(self)
        #Sets the name of the widget
        
        try:
            TaskIDs=ExecuteCommand("SELECT task_id FROM tasks WHERE CheckIfToday(task_duedate)=1 AND task_completed=0")
        except :
            pass
        else:
            for IDTuples in TaskIDs:
                ID=IDTuples[0]
                self.AddTaskToWidget(cl.Task.Instances[ID])
        self.setObjectName(u"TaskTodayWidget")

    
    def AddTaskToWidget(self,TaskObject: cl.Task):
        
        frame=QtWidgets.QFrame(self.ui.ScrollAreaContentsForTaskWidgets)
        framelayout=QtWidgets.QGridLayout()
        framelayout.addWidget(TaskWidget(frame,TaskObject))
        self.ui.VLayoutForTaskWidgets.addWidget(frame)

class LabelWidget(QtWidgets.QWidget):

    def __init__(self,frame,Label=None) -> None:
        super().__init__(frame)
        self.ui=LabelWidgetUI()
        self.ui.setupUi(frame)

        if Label==None:
            ErrorLog("WARNING : Label Widget Constructor called without provision of label")
            self.LabelID=-1
        else:
            self.SetInformation(Label)
    
    def SetInformation(self,Label: cl.Label):
        self.ui.EditColorButton.setStyleSheet(f"background : {HexFormat(Label.Color)}")
        self.ui.LabelNameEdit.setText(Label.Title)
        self.ui.LabelNameEdit.textChanged.connect(self.DisableReNameButton)
    
    def DisableReNameButton(self,Title):
        if cl.Label.ValidRename(Title):
            self.ui.ChangeNameButton.setEnabled()
        else:
            self.ui.ChangeNameButton.setDisabled()


class TaskWidget(QtWidgets.QWidget):

    #Lambda Function because python somehow doesn't have a method for this
    OrdinalTimeFunction=lambda n : str(n) + {1:'st',2:'nd',3:'rd'}.get(abs(n)%10,'th')

    def __init__(self,frame,Task=None) -> None:
        super().__init__(frame)
        self.ui=TaskWidgetUI()
        self.ui.setupUi(frame)
        
        if Task==None:
            ErrorLog("WARNING : TaskWidget Constructor called without providing a task")
            self.TaskID=-1
        else:
            self.SetInformation(Task)
    
    #Set Information is basically reconfiguring the label
    def SetInformation(self,TaskObject: cl.Task):
        
        #Sets the name of the object for easy identification
        self.setObjectName(f"TaskWidget{TaskObject.ID}")
        self.TaskID=TaskObject.ID
        self.ui.DeleteTaskButton.clicked.connect(lambda: self.parentWidget().deleteLater())
        self.ui.EditTaskButton.clicked.connect(lambda: TaskEditDialog().exec_() )
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

        #If the task is not given a duedate
        if Due==None:

            #Then Hide the days left part
            self.ui.DaysLeftDisplay.hide()
            self.ui.DaysLeftLabel.hide()
            Text=Title
        
        #The Task is not completed
        elif not Completed:
            
            DaysLeft=abs(Due-datetime.datetime.now()).days
            Text=f"Due On {Due.strftime(f'%a, {TaskWidget.OrdinalTimeFunction(Due.day)} %b %Y')} "+Title
            self.ui.DaysLeftDisplay.display(DaysLeft)
            #Show the labels if they're meant to be shown
            self.ui.DaysLeftDisplay.show()
            self.ui.DaysLeftLabel.show()
            
        #The Task is complete
        else:
            Text=f"Finished at {TaskObject.CompletedDate.strftime('%c')}"+Title
            #We can hide these labels since there's no need for a days left counter
            self.ui.DaysLeftDisplay.hide()
            self.ui.DaysLeftLabel.hide()
        
        #Set the Title text
        self.ui.TaskTitle_label.setText(Text)

        #Adds the Label Widget
        for Label in TaskObject.Labels:
            
            frame=QtWidgets.QFrame(self.ui.LabelsViewScrollContents)
            layout=QtWidgets.QHBoxLayout()
            layout.addWidget(LabelWidget(frame,Label))
            self.ui.LabelsHBoxLayout.addWidget(frame)

    #This needs the label widget to be ready
    def AddLabelWidget(self,LabelObject: cl.Label):
        frame=QtWidgets.QFrame(self.ui.LabelsViewScrollContents)
        layout=QtWidgets.QHBoxLayout()
        layout.addWidget(LabelWidget(frame,LabelObject))
        self.ui.LabelsHBoxLayout.addWidget(frame)

class SectionWidget(QtWidgets.QWidget):

    def __init__(self,frame,Section=None) -> None:
        super().__init__(frame)
        self.ui=SectionWidgetUI()
        self.ui.setupUi(frame)

        if Section==None:
            self.SectionID=-1
        else:
            self.SetInformation(Section)
    
    def SetInformation(self,Section: cl.Section):

        self.SectionID=Section.ID
        self.setObjectName(f"SectionWidget{self.SectionID}")

        #Button Widget
        self.ui.TaskAddButton.clicked.connect(lambda: self.AddTaskClicked())

        #If the section is a default section, hide the buttons to 
        #Delete and Show the Name of the Section
        if Section.DefaultSection==True:
            self.ui.SectionDeleteButton.hide()
            self.ui.SectionName.hide()
            self.ui.TaskAddButton.setShortcut("ctrl+t")
        else:
            self.ui.SectionName.setText(Section.Title)
        for Task in Section.Tasks.values():
            #Create the frame to add the widget to
            frame=QtWidgets.QFrame(self.ui.TasksContents)
            framelayout=QtWidgets.QGridLayout()
            framelayout.addWidget(TaskWidget(frame,Task))
            self.ui.VerticalLayoutForTaskWidgets.addWidget(frame)
            #Task Widget added to section Widget now

    
    def AddTaskClicked(self):
        Dialog=QtWidgets.QInputDialog(self)
        Dialog.resize(400,300)
        Dialog.setInputMode(QtWidgets.QInputDialog.TextInput)
        Dialog.setWindowTitle('Create Task')
        Dialog.setLabelText('Enter the Name of the Task')
        Dialog.setStyleSheet(StyleSheet)
        ok = Dialog.exec_()
        Title = Dialog.textValue()
        if ok:
            #If the user hit 'ok', then create the task
            #If the input is empty, then do nothing
            if not Title.strip(): return
            task=cl.Task(ParentSection=cl.Section.Instances[self.SectionID],TaskTitle=Title,DueDate=datetime.datetime.now()+datetime.timedelta(0,15))
            frame=QtWidgets.QFrame(self.ui.TasksContents)
            framelayout=QtWidgets.QGridLayout()
            framelayout.addWidget(TaskWidget(frame,task))
            self.ui.VerticalLayoutForTaskWidgets.addWidget(frame)
            #Section Widget added to project Widget now


class ProjectWidget(QtWidgets.QWidget):
    
    SignalDeleteProjectButton=QtCore.pyqtSignal(str)
    
    def __init__(self,frame,Project=None) -> None:
        super().__init__(frame)
        self.ui=ProjectWidgetUI()
        self.ui.setupUi(frame)

        if Project==None:
            ErrorLog("WARNING : ProjectWidget Constructor called without providing a project")
            self.ProjectID=-1
        else:
            self.SetInformation(Project)
        
        #Setup buttons
        self.ui.DeleteProject.setShortcut('Delete')
        self.ui.DeleteProject.clicked.connect(lambda: self.DeleteProject())

        self.ui.AddSection.setShortcut('ctrl+s')
    
    def DeleteProject(self):
        #Delete the Widgets parent frame
        parentwidget=self.parentWidget()
        parentwidget.deleteLater()
        self.SignalDeleteProjectButton.emit(f"AccessProjectButton_{self.ProjectID}")
        #Delete the Existing Project from the db
        (cl.Project.Instances[self.ProjectID]).DeleteProject()
        
    def SetInformation(self, ProjectObj: cl.Project):
        
        #Activate the buttons to do stuff
        self.ui.AddSection.clicked.connect(lambda: self.AddSectionClicked())
        self.ProjectID=ProjectObj.ID
        self.setObjectName(f"ProjectWidget{self.ProjectID}")
        
        #Sets the Label to display the Project name
        self.ui.ProjectName.setText(ProjectObj.Title)
        self.ui.ProjectName.setStyleSheet(f"background-color: {HexFormat(ProjectObj.Color)} ;")
        #Add the Section Widgets
        for Section in ProjectObj.Sections.values():
            #Create the frame to add the widget
            frame=QtWidgets.QFrame(self.ui.SectionWidgetArea)
            framelayout=QtWidgets.QGridLayout()
            framelayout.addWidget(SectionWidget(frame,Section))
            self.ui.LayoutToAddSections.addWidget(frame)
            #Section Widget added to project Widget now

    def AddSectionClicked(self):
        Dialog=QtWidgets.QInputDialog(self)
        Title,Ok=Dialog.getText(self,"Add Section","Section Name:",)
        if Ok:
            #If the user hit 'ok', then create the project
            #If the input is empty, then do nothing
            if not Title.strip(): return
            section=cl.Section(cl.Project.Instances[self.ProjectID],Title)
            frame=QtWidgets.QFrame(self.ui.SectionWidgetArea)
            framelayout=QtWidgets.QGridLayout()
            framelayout.addWidget(SectionWidget(frame,section))
            self.ui.LayoutToAddSections.addWidget(frame)
            #Section Widget added to project Widget now
class TaskEditDialog(QtWidgets.QDialog):

    ReturnSignal=QtCore.pyqtSignal(bool)
    
    def __init__(self,TaskTitle=None,TaskDesc=None,TaskDueDate=None,ReminderState=None) -> None:
        super().__init__()
        #Set it to be a modal dialog
        self.setModal(True)
        self.ui=TaskEditUI()
        self.ui.setupUi(self)
        self.setStyleSheet(StyleSheet)

        
        
