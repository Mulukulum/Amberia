import datetime
import sys
from os.path import dirname
import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from Codebase.Functions.Database import ExecuteCommand,ExecuteScript
from Codebase.GUI.UserSettings import Stylesheet,MinTaskDispHt,MinSecDispHt,HelpBehaviour,sidebarfactor,ProjMinHt,Defaults

FilePath=f'//StyleSheet//{Stylesheet}'
path=dirname(__file__)+FilePath
with open(path) as f:
    StyleSheet=f.read()
from Codebase.Classes import classes as cl
from Codebase.GUI.UI_Classes.TasksTodayWindow import TaskTodayUI
from Codebase.GUI.UI_Classes.TaskWidget import TaskWidgetUI
from Codebase.GUI.UI_Classes.HelpWidget import HelpWidgetUI
from Codebase.GUI.UI_Classes.LabelEditor import LabelWidgetUI
from Codebase.GUI.UI_Classes.ProjectEditor import ProjectEditDialog 
from Codebase.GUI.UI_Classes.ProjectWidget import ProjectWidgetUI
from Codebase.GUI.UI_Classes.SectionWidget import SectionWidgetUI
from Codebase.GUI.UI_Classes.Settings import SettingsUI
from Codebase.GUI.UI_Classes.TaskEdit import TaskEditUI

from Codebase.ErrorLogs.logging import ErrorLog
from Codebase.Functions.Colors import HexFormat

class TodayTasksWidget(QtWidgets.QWidget):
    #Signal to make a new instance of the widget
    SortSignal=QtCore.pyqtSignal(int)

    def __init__(self,frame,SortBy) -> None:
        super().__init__(frame)
        self.ui=TaskTodayUI()
        self.frame=frame
        self.ui.setupUi(self)
        #Button Setup
        self.ui.SortNameButton.clicked.connect(lambda: self.SortSignal.emit(0))
        self.ui.SortProjectButton.clicked.connect(lambda : self.SortSignal.emit(1))
        self.ui.SortPriorityButton.clicked.connect(lambda : self.SortSignal.emit(2))
        self.ui.SortNameButton.setStyleSheet(self.ui.SortNameButton.styleSheet()+"; font-size: 14px ; ")
        self.ui.SortProjectButton.setStyleSheet(self.ui.SortProjectButton.styleSheet()+"; font-size: 14px ; ")
        self.ui.SortPriorityButton.setStyleSheet(self.ui.SortPriorityButton.styleSheet()+"; font-size: 14px ; ")
        #Sets the SQL Queries
        NameSort="SELECT task_id FROM tasks WHERE CheckIfToday(task_duedate)=1 AND task_completed=0 ORDER BY task_title"
        ProjectSort="SELECT task_id FROM tasks WHERE CheckIfToday(task_duedate)=1 AND task_completed=0 ORDER BY task_projectid"
        PrioritySort="SELECT task_id FROM tasks WHERE CheckIfToday(task_duedate)=1 AND task_completed=0 ORDER BY task_priority"
        Queries=(NameSort,ProjectSort,PrioritySort)
        try:
            TaskIDs=ExecuteCommand(Queries[SortBy])
        except:
            ErrorLog("CRITICAL: TODAY TASK(S) LOOKUP FAILED. Likely Error due to issue with UDF in Functions\Database.py")
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
    MinimumTaskHeight=MinTaskDispHt

    def __init__(self,frame,Task: cl.Task=None) -> None:
        super().__init__(frame)
        self.ui=TaskWidgetUI()
        self.ui.setupUi(frame)
        frame.setMinimumHeight(self.MinimumTaskHeight)
        #install event filter for taskdesc edit
        self.ui.TaskDescription.installEventFilter(self)

        #Set StyleSheets
        frame.setStyleSheet(frame.styleSheet()+".QFrame:hover { background-color: #7a7a7a;}")
        self.ui.TaskDescription.setStyleSheet("color: #c9c15f ; font-size: 16px ;")
        self.ui.ReminderBox.setStyleSheet("color: #c9c15f ; ")
        self.ui.PriorityLevelDisplay.setStyleSheet("color : #c9c15f ; ")
        self.ui.DaysLeftDisplay.setStyleSheet("color : #c9c15f ; ")
        self.ui.EditTaskButton.setStyleSheet(self.ui.EditTaskButton.styleSheet()+"; font-size: 16px ; ")
        self.ui.ReminderBox.setStyleSheet(self.ui.ReminderBox.styleSheet()+"; font-size: 16px ; ")
        self.ui.DeleteTaskButton.setStyleSheet(self.ui.DeleteTaskButton.styleSheet()+"; font-size: 16px ; ")
        #Labels have their bg colors tied to priority level so its important to set that in the reconfigure function
        self.ui.TaskTitle_label.setStyleSheet(self.ui.TaskTitle_label.styleSheet()+f"; font-size: 16px ; background-color: {HexFormat(cl.Priority.ColorOfLevel(Task.PriorityLevel))} ")
        self.ui.DaysLeftLabel.setStyleSheet(self.ui.DaysLeftLabel.styleSheet()+f"; font-size: 16px ; background-color: {HexFormat(cl.Priority.ColorOfLevel(Task.PriorityLevel))}")
        self.ui.PriorityLabel.setStyleSheet(self.ui.PriorityLabel.styleSheet()+f"; font-size: 16px ; background-color: {HexFormat(cl.Priority.ColorOfLevel(Task.PriorityLevel))}")
        
        #Set the style of the LCD Screens
        self.ui.PriorityLevelDisplay.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ui.DaysLeftDisplay.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

        #Set Signals and slots
        self.ui.ReminderBox.stateChanged.connect(self.ReminderStateChanged)
        self.ui.DeleteTaskButton.clicked.connect(lambda: self.TaskDeleteButtonClicked(Task))
        self.ui.EditTaskButton.clicked.connect(lambda: self.TaskEditButtonClicked())
        #Set task information
        if Task==None:
            ErrorLog("WARNING : TaskWidget Constructor called without providing a task")
            self.TaskID=-1
        else:
            self.SetInformation(Task)
    
    def ReminderStateChanged(self,ShowReminder: int):
        Task=cl.Task.Instances[self.TaskID]
        if ShowReminder: Task.SetReminderState(1)
        else: Task.SetReminderState(0)
    
    def TaskDescChanged(self,Text: str):
        Task=cl.Task.Instances[self.TaskID]
        Task.UpdateTaskDesc(Text)

    #Set Information is basically reconfiguring the taskui
    def SetInformation(self,TaskObject: cl.Task):
        #Sets the name of the object for easy identification
        self.setObjectName(f"TaskWidget{TaskObject.ID}")
        self.TaskID=TaskObject.ID
        #Sets the Display to show priority Level
        self.ui.PriorityLevelDisplay.display(TaskObject.PriorityLevel)
        #Sets the Description to the Description of the Task
        if TaskObject.TaskDesc!=None:
            self.ui.TaskDescription.setText(TaskObject.TaskDesc)
        else:
            self.ui.TaskDescription.setPlaceholderText(u'Describe Your Task or Add Notes Here') 
        #Get the Title of the Task
        Title=TaskObject.TaskTitle
        Due=TaskObject.DueDate
        Completed=TaskObject.Completed
        self.ui.TaskTitle_label.setStyleSheet(self.ui.TaskTitle_label.styleSheet()+f"; font-size: 16px ; background-color: {HexFormat(cl.Priority.ColorOfLevel(TaskObject.PriorityLevel))} ")
        self.ui.DaysLeftLabel.setStyleSheet(self.ui.DaysLeftLabel.styleSheet()+f"; font-size: 16px ; background-color: {HexFormat(cl.Priority.ColorOfLevel(TaskObject.PriorityLevel))}")
        self.ui.PriorityLabel.setStyleSheet(self.ui.PriorityLabel.styleSheet()+f"; font-size: 16px ; background-color: {HexFormat(cl.Priority.ColorOfLevel(TaskObject.PriorityLevel))}")
        #If the task is not given a duedate
        if Due==None:
            #Then Hide the days left part
            self.ui.DaysLeftDisplay.hide()
            self.ui.DaysLeftLabel.hide()
            Text=Title
        #If the Task is not completed
        elif not Completed:
            DaysLeft=abs(Due-datetime.datetime.now()).days
            Text=(Title[:20]+'... ' if len(Title)>20 else Title)+f" Due On {Due.strftime(f'%a, {TaskWidget.OrdinalTimeFunction(Due.day)} %b %Y')} "
            self.ui.DaysLeftDisplay.display(DaysLeft)
            #Show the labels if they're meant to be shown
            self.ui.DaysLeftDisplay.show()
            self.ui.DaysLeftLabel.show()
        #If the Task is complete
        else:
            Text=f"Finished at {TaskObject.CompletedDate.strftime('%c')}"+Title
            #We can hide these labels since there's no need for a days left counter
            self.ui.DaysLeftDisplay.hide()
            self.ui.DaysLeftLabel.hide()
        #Set the Title text
        self.ui.TaskTitle_label.setText(Text)
        self.ui.TaskTitle_label.setAlignment(QtCore.Qt.AlignCenter)
        if TaskObject.ShowReminder:
            self.ui.ReminderBox.setChecked(True)
            TaskObject.SetReminderState(1)
        else:
            self.ui.ReminderBox.setChecked(False)
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

    def eventFilter(self, TaskDescObj: QtWidgets.QTextBrowser, Event: QtCore.QEvent) -> bool:        
        if TaskDescObj==self.ui.TaskDescription and Event.type()==QtCore.QEvent.FocusOut:
            self.TaskDescChanged(self.ui.TaskDescription.toPlainText())
        return super().eventFilter(TaskDescObj,Event)

    def TaskEditButtonClicked(self):
        #First, create the Dialog to popup
        Task=cl.Task.Instances[self.TaskID]
        TaskEditDialog(Task=Task,TaskTitle=Task.TaskTitle,TaskDesc=Task.TaskDesc,TaskDueDate=Task.DueDate,PriorityLevel=Task.PriorityLevel)
        self.SetInformation(Task)
    
    def TaskDeleteButtonClicked(self,Task: cl.Task):
        Task.DeleteTask()
        self.parentWidget().deleteLater()

class SectionWidget(QtWidgets.QWidget):
    MinimumSectionHeight=MinSecDispHt

    #1 if you want to set it to today

    def __init__(self,frame,Section: cl.Section=None) -> None:
        super().__init__(frame)
        self.ui=SectionWidgetUI()
        self.ui.setupUi(frame)
        frame.setMinimumHeight(self.MinimumSectionHeight)
        #Main setup completed
        #StyleSheets
        frame.setStyleSheet(frame.styleSheet()+".QFrame:hover {background-color: #2a3364}")
        self.ui.SectionName.setStyleSheet(self.ui.SectionName.styleSheet()+f"; font-size: 14px ; background-color: {HexFormat(Section.ParentProject.Color)}")
        self.ui.TaskAddButton.setStyleSheet(self.ui.TaskAddButton.styleSheet()+f"; font-size: 14px ; ")
        self.ui.SectionDeleteButton.setStyleSheet(self.ui.SectionDeleteButton.styleSheet()+f"; font-size: 14px ; ")
        #Button shortcuts
        if Section.IsDefaultSection : self.ui.TaskAddButton.setShortcut("ctrl+t")
        #Signals and slots
        self.ui.SectionDeleteButton.clicked.connect(lambda: self.DeleteSectionWidget())
        self.ui.TaskAddButton.clicked.connect(lambda: self.AddTaskClicked())
        if Section==None:
            self.SectionID=-1
        else:
            self.SetInformation(Section)
    
    def SetInformation(self,Section: cl.Section):
        self.SectionID=Section.ID
        self.setObjectName(f"SectionWidget{self.SectionID}")
        #If the section is a default section, hide the buttons to 
        #Delete and Show the Name of the Section
        if Section.IsDefaultSection==True:
            self.ui.SectionDeleteButton.hide()
            self.ui.SectionName.hide()
        else:
            self.ui.SectionName.setText(Section.Title)
            self.ui.SectionName.setAlignment(QtCore.Qt.AlignCenter)
        for Task in Section.Tasks.values():
            #Create the frame to add the widget to
            frame=QtWidgets.QFrame(self.ui.TasksContents)
            frame.setObjectName("framefortask")
            framelayout=QtWidgets.QGridLayout()
            framelayout.addWidget(TaskWidget(frame,Task))
            self.ui.VerticalLayoutForTaskWidgets.addWidget(frame)
            #Task Widget added to section Widget now

    def AddTaskClicked(self):
        Dialog=QtWidgets.QInputDialog(self)
        Dialog.resize(300,500)
        Dialog.setStyleSheet("font-size: 16px")
        Dialog.setInputMode(QtWidgets.QInputDialog.TextInput)
        Dialog.setWindowTitle('Create Task')
        Dialog.setLabelText('Enter the Name of the Task')
        Dialog.setStyleSheet(StyleSheet+'; font-size: 16px')
        Ok = Dialog.exec_()
        Title = Dialog.textValue()
        if Ok:
            #If the user hit 'ok', then create the task
            #If the input is empty, then do nothing
            if not Title.strip(): return
            task=cl.Task(ParentSection=cl.Section.Instances[self.SectionID],TaskTitle=Title,DueDate=None)
            frame=QtWidgets.QFrame(self.ui.TasksContents)
            framelayout=QtWidgets.QGridLayout()
            framelayout.addWidget(TaskWidget(frame,task))
            self.ui.VerticalLayoutForTaskWidgets.addWidget(frame)
            #Section Widget added to project Widget now
        
    def DeleteSectionWidget(self):
        cl.Section.Instances[self.SectionID].DeleteSection()
        self.parentWidget().deleteLater()
class ProjectEditWidget(QtWidgets.QDialog):

    def __init__(self,ProjectName):
        super().__init__()
        self.ChangeColor=False
        self.Color=-1
        self.ui=ProjectEditDialog()
        self.ui.setupUi(self,ProjectName)
        self.setStyleSheet(StyleSheet)
        self.ui.ToggleColorEdit.toggled.connect(self.ToggleColorEdit)
        self.ui.ColorEdit.currentColorChanged.connect(self.UpdateCurrentColor)
    
    def UpdateCurrentColor(self):
        self.Color=int(self.ui.ColorEdit.currentColor().name().strip('#'),16)
    
    def ToggleColorEdit(self):
        if self.ChangeColor:
            self.ChangeColor=False
            self.ui.ColorEdit.setDisabled(True)
        else:
            self.ChangeColor=True
            self.ui.ColorEdit.setDisabled(False)

class ProjectWidget(QtWidgets.QWidget):

    SignalDeleteProjectButton=QtCore.pyqtSignal(str)
    SignalEditProjectButton=QtCore.pyqtSignal(str,str,str)

    def __init__(self,frame,Project=None) -> None:
        super().__init__(frame)
        self.ui=ProjectWidgetUI()
        self.ui.setupUi(frame)
        if Project==None:
            ErrorLog("WARNING : ProjectWidget Constructor called without providing a project")
            self.ProjectID=-1
        else:
            self.SetInformation(Project)
        #Stylesheets
        self.ui.ProjectName.setStyleSheet(self.ui.ProjectName.styleSheet()+"; font-size: 14px")
        self.ui.EditDetails.setStyleSheet(self.ui.EditDetails.styleSheet()+"; font-size: 14px")
        self.ui.AddSection.setStyleSheet(self.ui.AddSection.styleSheet()+"; font-size: 14px")
        self.ui.DeleteProject.setStyleSheet(self.ui.DeleteProject.styleSheet()+"; font-size: 14px")
        #Setup buttons
        self.ui.DeleteProject.clicked.connect(lambda: self.DeleteProject())
        self.ui.EditDetails.clicked.connect(lambda: self.EditButtonClick())
        #Shortcuts
        self.ui.DeleteProject.setShortcut('Delete')
        self.ui.AddSection.setShortcut('ctrl+a')

    def DeleteProject(self):
        #Emit the signal to delete the project button
        self.SignalDeleteProjectButton.emit(f"AccessProjectButton_{self.ProjectID}")
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
    def EditButtonClick(self):
        dialog=ProjectEditWidget(self.ui.ProjectName.text())
        Ok=dialog.exec_()
        if Ok:
            Proj=cl.Project.Instances[self.ProjectID]
            Title=dialog.ui.lineEdit.text()
            if dialog.ChangeColor:
                Proj.SetColor(dialog.Color)
            else:
                dialog.Color=Proj.Color
            Proj.SetName(Title.strip())
            self.ui.ProjectName.setText(Title.strip())
            self.ui.ProjectName.setStyleSheet(self.ui.ProjectName.styleSheet()+f'; background-color:{HexFormat(dialog.Color)};')
            self.SignalEditProjectButton.emit(f"AccessProjectButton_{self.ProjectID}",Title.strip(),HexFormat(dialog.Color))

    def AddSectionClicked(self):
        Dialog=QtWidgets.QInputDialog(self)
        Dialog.setInputMode(QtWidgets.QInputDialog.TextInput)
        Dialog.setWindowTitle('Create Section')
        Dialog.setLabelText('Enter the Name of the Section')
        Dialog.setStyleSheet(StyleSheet+'; font-size: 16px')
        Ok = Dialog.exec_()
        Title = Dialog.textValue()
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

    def __init__(self,Task: cl.Task,PriorityLevel,TaskTitle=None,TaskDesc=None,TaskDueDate: datetime.datetime=None) -> None:
        super().__init__()
        #Set it to be a modal dialog
        self.EditDueDate=False
        self.setModal(True)
        self.ui=TaskEditUI()
        self.setStyleSheet(StyleSheet)
        self.ui.setupUi(self)
        self.setWindowTitle("Edit Task")
        self.resize(600,300)
        #Sets the date for the datetime edit
        if TaskDueDate==None:
            TaskDueDate=datetime.datetime.now()
        #Setting the displays
        self.ui.DueDateEdit.setDisplayFormat("dd-MM-yyyy HH:mm:ss")
        self.ui.DueDateEdit.setDateTime(QtCore.QDateTime.fromString(str(TaskDueDate)[0:19],"yyyy-MM-dd HH:mm:ss"))
        self.ui.PriorityLevelEdit.setValue(PriorityLevel)
        self.ui.TaskTitleEdit.setText(TaskTitle)
        if TaskDesc!=None: self.ui.TaskDescEdit.setText(TaskDesc)
        self.ui.EnableDueDateButton.toggled.connect(self.Toggle)

        #Stylesheets
        self.ui.DueDateEdit.setStyleSheet(" font-size: 16px ; ")
        self.ui.PriorityLevelEdit.setStyleSheet(" font-size: 16px ; ")
        self.ui.TaskTitleEdit.setStyleSheet(" font-size: 16px ; ")
        self.ui.TaskDescEdit.setStyleSheet( "font-size: 16px ; ")
        self.ui.TaskDueLabel.setStyleSheet(" font-size: 16px ; ")
        self.ui.PriorityLabel.setStyleSheet(" font-size: 16px ; ")
        self.ui.CancelButton.setStyleSheet(" font-size: 16px ; ")
        self.ui.SubmitButton.setStyleSheet(" font-size: 16px ; ")
        self.ui.EnableDueDateButton.setStyleSheet(" font-size: 16px ; ")
        Ok = self.exec_()
        if Ok:
            newpr=self.ui.PriorityLevelEdit.value()
            newtitle=self.ui.TaskTitleEdit.text()
            newdesc=self.ui.TaskDescEdit.toPlainText()
            if self.EditDueDate:
                newduedate=self.ui.DueDateEdit.dateTime()
                newduedate=newduedate.toPyDateTime()
                Task.ReConfigureTask(newtitle,newdesc,newpr,DueDate=newduedate)
            else:
                Task.ReConfigureTask(newtitle,newdesc,newpr)
    
    def Toggle(self):
        if self.EditDueDate:
            self.EditDueDate=False
            self.ui.DueDateEdit.setDisabled(True)
        else:
            self.EditDueDate=True
            self.ui.DueDateEdit.setDisabled(False)
        
        
        

class SettingsWidget(QtWidgets.QWidget):

    ThemesDictionary={
        "DefaultTheme":"Amberia.qss",
        "DayTheme":"Day.qss",
        "Phantasmagoric":"Phantasmagoric.qss",
        "TwilightTheme":"Twilight.qss",
        }
    #To be modified after the themes are made
    ThemesBackground={
        "DefaultTheme":"#2a3364",
        "DayTheme":"#cc0000",
        "Phantasmagoric":"#18191A",
        "TwilightTheme":"#FD5E53",
    }

    def __init__(self,frame,MainWindow) -> None:
        super().__init__(frame)
        self.ui=SettingsUI()
        self.frame=frame
        self.setStyleSheet(StyleSheet)
        self.ui.setupUi(self)
        self.MW=MainWindow
        #Setup the Constants
        self.SelectedTheme=None
        self.ResetPrValues=False
        self.ResetTheme=False
        #Settings margins and borders
        self.ui.ColorSettingsLabel.setStyleSheet(f'{self.ui.ColorSettingsLabel.styleSheet()} ; margin-right: 500% ; margin-left: 500% ; border-radius: 12%')
        #Signals and slots setup
        self.ui.SaveChangesRestart.clicked.connect(self.SaveChangesRestart)
        self.ui.SaveChanges.clicked.connect(self.SaveChanges)
        self.ui.CancelChanges.clicked.connect(MainWindow.ShowTasksTodayWidget)
        self.ui.ResetButton.clicked.connect(self.ResetDisplayBehaviours)
        self.ui.DayTheme.clicked.connect(self.DayTheme)
        self.ui.Phantasmagoric.clicked.connect(self.Phantasmagoric)
        self.ui.TwilightTheme.clicked.connect(self.TwilightTheme)
        self.ui.DefaultTheme.clicked.connect(self.DefaultTheme)
        #Priority-Colors
        self.ui.Pr1.clicked.connect(lambda : self.ChangePrColor(1))
        self.ui.Pr2.clicked.connect(lambda : self.ChangePrColor(2))
        self.ui.Pr3.clicked.connect(lambda : self.ChangePrColor(3))
        self.ui.Pr4.clicked.connect(lambda : self.ChangePrColor(4))
        self.ui.Pr5.clicked.connect(lambda : self.ChangePrColor(5))
        self.ui.Pr6.clicked.connect(lambda : self.ChangePrColor(6))
        self.ui.Pr7.clicked.connect(lambda : self.ChangePrColor(7))
        self.ui.Pr8.clicked.connect(lambda : self.ChangePrColor(8))
        self.ui.Pr9.clicked.connect(lambda : self.ChangePrColor(9))
        self.ui.Pr10.clicked.connect(lambda: self.ChangePrColor(10))
        self.ui.DefaultValueButton.clicked.connect(lambda : self.ResetPriorityColors())
        #Set the values into the corresponding displays
        self.SetPriorityColors()
        try:
            res=ExecuteCommand("SELECT stylesheet, mintaskdispheight, minsecdispheight, projectminheight , sidebarfactor, showhelp FROM settings WHERE def=1")[0]
        except:
            res=tuple()
        if len(res)==0:
            ExecuteCommand("DELETE FROM settings")
            ExecuteCommand(f"INSERT INTO SETTINGS VALUES{(0,)+Defaults}")
            ExecuteCommand(f"INSERT INTO SETTINGS VALUES{(1,)+Defaults}")
            res=Defaults
        Stylsht,MinTaskDispHt,MinSecDispHt,ProjMinHt,sidebarfactor,HelpBehaviour=res
        #Help behaviour setup
        if HelpBehaviour:
            self.ui.HelpBehaviour.setChecked(True)
        else:
            self.ui.HelpBehaviour.setChecked(False)
        #Themes setup
        for buttonname,ss in self.ThemesDictionary.items():
            if ss==Stylsht:
                selectedss=buttonname
                break
        self.SelectedTheme=self.findChild(QtWidgets.QPushButton,selectedss)
        self.SelectedTheme.setStyleSheet(f"background-color: {self.ThemesBackground[self.SelectedTheme.objectName()]}")
        #Values Setup
        self.ui.TaskDispHeight.setValue(MinTaskDispHt)
        self.ui.SecDispHeight.setValue(MinSecDispHt)
        self.ui.ProjButtonHeight.setValue(ProjMinHt)
        self.ui.SidebarScaleFactor.setValue(sidebarfactor)

    def ResetDisplayBehaviours(self):
        #Default Values Set
        res=Defaults[1::]
        MinTaskDispHt,MinSecDispHt,ProjMinHt,sidebarfactor,HelpBehaviour=res
        #Help behaviour setup
        if HelpBehaviour:
            self.ui.HelpBehaviour.setChecked(True)
        else:
            self.ui.HelpBehaviour.setChecked(False)
        #Values Setup
        self.ui.TaskDispHeight.setValue(MinTaskDispHt)
        self.ui.SecDispHeight.setValue(MinSecDispHt)
        self.ui.ProjButtonHeight.setValue(ProjMinHt)
        self.ui.SidebarScaleFactor.setValue(sidebarfactor)


    def SaveChangesRestart(self):
        #Get all the values
        TaskDispHt=self.ui.TaskDispHeight.value()
        SectionDispHt=self.ui.SecDispHeight.value()
        ProjButtonHt=self.ui.ProjButtonHeight.value()
        SidebarScale=self.ui.SidebarScaleFactor.value()
        HelpBehaviour=self.ui.HelpBehaviour.isChecked()
        if self.SelectedTheme!=None: 
            StyleSheet=self.ThemesDictionary.get(self.SelectedTheme.objectName())
        else: 
            StyleSheet=Stylesheet
        ExecuteCommand("""UPDATE settings SET stylesheet=?,
        mintaskdispheight=? , minsecdispheight=? , projectminheight=? ,
        sidebarfactor=? , showhelp=? WHERE def=1 """,
        (StyleSheet, TaskDispHt, SectionDispHt,ProjButtonHt,SidebarScale,HelpBehaviour))
        #Changes successfully saved, now the restart is initiated
        self.MW.Restart()

    def SaveChanges(self):
        #Get all the values
        from random import choice
        self.ui.SaveChanges.setText("Changes Saved.." if choice(range(40)) else "Too real da🔥" )
        QtCore.QTimer.singleShot(700,lambda: self.RevertText())
        TaskDispHt=self.ui.TaskDispHeight.value()
        SectionDispHt=self.ui.SecDispHeight.value()
        ProjButtonHt=self.ui.ProjButtonHeight.value()
        SidebarScale=self.ui.SidebarScaleFactor.value()
        HelpBehaviour=self.ui.HelpBehaviour.isChecked()
        if self.SelectedTheme!=None: 
            StyleSheet=self.ThemesDictionary.get(self.SelectedTheme.objectName())
        else: 
            StyleSheet=Stylesheet
        ExecuteCommand("""UPDATE settings SET stylesheet=?,
        mintaskdispheight=? , minsecdispheight=? , projectminheight=? ,
        sidebarfactor=? , showhelp=? WHERE def=1 """,
        (StyleSheet, TaskDispHt, SectionDispHt,ProjButtonHt,SidebarScale,HelpBehaviour))
        #No restart is called here

    def DayTheme(self):
        if self.SelectedTheme!=None:
            self.SelectedTheme.setStyleSheet(StyleSheet)
        self.SelectedTheme=self.ui.DayTheme
        self.SelectedTheme.setStyleSheet(f"background-color: {self.ThemesBackground[self.SelectedTheme.objectName()]}")
    
    def TwilightTheme(self):
        if self.SelectedTheme!=None:
            self.SelectedTheme.setStyleSheet(StyleSheet)
        self.SelectedTheme=self.ui.TwilightTheme
        self.SelectedTheme.setStyleSheet(f"background-color: {self.ThemesBackground[self.SelectedTheme.objectName()]}")

    def Phantasmagoric(self):
        if self.SelectedTheme!=None:
            self.SelectedTheme.setStyleSheet(StyleSheet)
        self.SelectedTheme=self.ui.Phantasmagoric
        self.SelectedTheme.setStyleSheet(f"background-color: {self.ThemesBackground[self.SelectedTheme.objectName()]}")
    
    def DefaultTheme(self):
        if self.SelectedTheme!=None:
            self.SelectedTheme.setStyleSheet(StyleSheet)
        self.SelectedTheme=self.ui.DefaultTheme
        self.SelectedTheme.setStyleSheet(f"background-color: {self.ThemesBackground[self.SelectedTheme.objectName()]}")

    def SetPriorityColors(self):
        self.ui.Pr1.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(1))}")
        self.ui.Pr2.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(2))}")
        self.ui.Pr3.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(3))}")
        self.ui.Pr4.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(4))}")
        self.ui.Pr5.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(5))}")
        self.ui.Pr6.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(6))}")
        self.ui.Pr7.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(7))}")
        self.ui.Pr8.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(8))}")
        self.ui.Pr9.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(9))}")
        self.ui.Pr10.setStyleSheet(f"background-color: {HexFormat(cl.Priority.ColorOfLevel(10))}")

    def PopupColorDialog(self):
        dialog=QtWidgets.QColorDialog(self)
        dialog.setModal(True)
        Ok=dialog.exec_()
        if Ok:
            return dialog.selectedColor().name()
        
    
    def ChangePrColor(self,PrLevel):
        color=self.PopupColorDialog()
        if color==None: return
        self.findChild(QtWidgets.QPushButton,f"Pr{PrLevel}").setStyleSheet(f"background-color: {color}")
        cl.Priority.UpdateColor(PrLevel,int(str(color).strip('# '),16))
        #Colors updated now
    
    def ResetPriorityColors(self):
        #Runs the script to set the default priority colors
        ExecuteScript(cl.Priority.ScriptSetDefaultColors)
        cl.Priority.ColorCache=cl.Priority.DefaultPriorityColors
        #Set the priority Colors again
        self.SetPriorityColors()
    
    def RevertText(self):
        try:
            self.ui.SaveChanges.setText("Save Changes")
        except: ...
        
class HelpWidget(QtWidgets.QWidget):
    def __init__(self,frame) -> None:
        super().__init__(frame)
        self.ui=HelpWidgetUI()
        self.ui.setupUi(self)
