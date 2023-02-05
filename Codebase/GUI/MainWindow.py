#Required Imports
import datetime
import sys
import os.path
import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Codebase.Functions.Database import ExecuteCommand
from Codebase.Functions.Colors import HexFormat
from Codebase.Classes import classes as cl
from Codebase.GUI.UI_Classes.AmberMainWin import AmberWindowUI
from Codebase.GUI.Widgets import (
    TodayTasksWidget, ProjectWidget,SettingsWidget, HelpWidget,StyleSheet, ProjMinHt, HelpBehaviour
    )

class AmberMainWindow(QtWidgets.QMainWindow):

    ProjectButtonMinimumHeight=ProjMinHt
    
    try:
        SideBarScaleFactor=ExecuteCommand("SELECT sidebarfactor FROM settings WHERE def=1")[0][0]
    except:
        SideBarScaleFactor=0.235
    #Constant that is modified when needed
    # 0 implies quit and 678452056 implies that user has requested a restart
    EXITCODE=0

    def __init__(self) -> None:
        #Sets up the mainwindow class
        super().__init__()
        #Mainwindow Ui Setup
        self.ui=AmberWindowUI()
        self.ui.setupUi(self)
        self.setStyleSheet(StyleSheet)
        self.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__)+r"\\UI_Files\\AppIcon.ico"))
        self.setWindowTitle("Amberia")
        self.WidgetFrame=QtWidgets.QFrame()
        #Basic UI Setup Done
        #Set the Shortcuts for the Buttons
        self.ui.TasksTodayButton.setShortcut("ctrl+r")
        self.ui.CreateProjectButton.setShortcut("ctrl+n")
        self.ui.SettingsButton.setShortcut("ctrl+s")
        self.ui.HelpButton.setShortcut("ctrl+h")

        #Set Minimum Sizes for the widgets
        self.ui.ProjectsLabel.setMaximumHeight(200)
        self.ui.ProjectsLabel.setMinimumHeight(40)
        self.ui.TasksTodayButton.setMaximumHeight(300)
        self.ui.TasksTodayButton.setMinimumHeight(40)
        self.ui.CreateProjectButton.setMaximumHeight(300)
        self.ui.CreateProjectButton.setMinimumHeight(40)
        self.ui.HelpButton.setMaximumHeight(200)
        self.ui.HelpButton.setMinimumHeight(40)
        

        #Set the stylesheets
        self.ui.CurrentWidgetTitleLabel.setStyleSheet(self.ui.CurrentWidgetTitleLabel.styleSheet()+"; font-size: 24px")
        self.ui.ProjectsLabel.setStyleSheet(self.ui.ProjectsLabel.styleSheet()+"font-size: 20px")
        self.ui.TasksTodayButton.setStyleSheet(self.ui.TasksTodayButton.styleSheet()+" ; font-size: 24px ;")
        self.ui.CreateProjectButton.setStyleSheet(self.ui.CreateProjectButton.styleSheet()+"; font-size: 24px ;")
        self.ui.HelpButton.setStyleSheet(self.ui.HelpButton.styleSheet()+"; font-size: 24px ;")
        
        #Set the connections of the buttons
        self.ui.SettingsButton.clicked.connect(self.ShowSettingsWidget)
        self.ui.TasksTodayButton.clicked.connect(self.ShowTasksTodayWidget)
        self.ui.CreateProjectButton.clicked.connect(self.AddProjectButtonClicked)
        self.ui.HelpButton.clicked.connect(self.ShowHelpWidget)

        #Sets the default widget
        if not HelpBehaviour:
            self.ShowTasksTodayWidget()
        else:
            self.ShowHelpWidget()

        #Makes the buttons for the existing projects
        self.RetrieveFromDB()
        #Show Window
        
        self.showMaximized()
    
    def resizeEvent(self, Event: QtGui.QResizeEvent) -> None:
        self.ui.ProjectScrollArea.setMinimumWidth(int(Event.size().width()*self.SideBarScaleFactor))
        return super().resizeEvent(Event)
    
    def RemoveProjectButton(self,ObjectName: str):
        button=self.findChildren(QtWidgets.QPushButton,ObjectName)[0]
        button.deleteLater()
        self.ui.SettingsButton.click()
    
    def EditProjectButtonName(self,ObjectName: str,Title: str,Color: str):
        button=self.findChildren(QtWidgets.QPushButton,ObjectName)[0]
        button.setText(Title)
        button.setStyleSheet(f"background-color: {Color} ; font-size: 20px ; ")
    
    def RetrieveFromDB(self):
        #Function to update the UI with project buttons
        for Project in cl.Project.Instances.values():
            self._AddProjectFromDB(Project)
    
    def _AddProjectFromDB(self,Proj: cl.Project):
        #Create the button
        button=QtWidgets.QPushButton(self.ui.ProjectContents)
        button.setObjectName(f"AccessProjectButton_{Proj.ID}")
        button.setText(Proj.Title)
        button.setMinimumHeight(self.ProjectButtonMinimumHeight)
        button.setStyleSheet(f"background-color: {HexFormat(Proj.Color)} ; font-size: 20px ; ")
        button.clicked.connect(lambda: self.ShowProjectWidget(Proj))
        #Show the button
        self.ui.ButtonList.addWidget(button)

    def AddProjectButtonClicked(self):
        #Popup the dialog
        Dialog=QtWidgets.QInputDialog(self)
        Dialog.resize(400,300)
        Dialog.setInputMode(QtWidgets.QInputDialog.TextInput)
        Dialog.setWindowTitle('Add Project')
        Dialog.setLabelText('Enter Project Name')
        Dialog.setStyleSheet(Dialog.styleSheet()+"; font-size:16px")
        Ok = Dialog.exec_()
        Title = Dialog.textValue()
        if Ok:
            #If the user hit 'ok', then create the project
            #If the input is empty, then do nothing
            if not Title.strip(): return
            Title=Title.lstrip('_')
            Proj=cl.Project(Title)
            button=QtWidgets.QPushButton(self.ui.ProjectContents)
            button.setObjectName(f"AccessProjectButton_{Proj.ID}")
            button.setText(Proj.Title)
            button.setMinimumHeight(self.ProjectButtonMinimumHeight)
            button.setStyleSheet(f"background-color: {HexFormat(Proj.Color)} ; font-size: 20px ; ")
            self.ui.ButtonList.addWidget(button)
            button.clicked.connect(lambda: self.ShowProjectWidget(Proj))
            button.click()
            
    def ShowProjectWidget(self,ProjectObj):
        #Delete the current Widget that is shown and add the other widget after creating it
        self.WidgetFrame.deleteLater()
        self.SetTasksTodayWidgetTitle()
        FrameForMainWidget=QtWidgets.QFrame(self.ui.MainWidgetFrame)
        framelayout=QtWidgets.QGridLayout()
        #Connect the signals and slots
        ProjWid=ProjectWidget(frame=FrameForMainWidget, Project=ProjectObj)
        ProjWid.SignalDeleteProjectButton.connect(lambda objname: self.RemoveProjectButton(objname))
        ProjWid.SignalEditProjectButton.connect(lambda Objname,Title,Color: self.EditProjectButtonName(Objname,Title,Color))

        framelayout.addWidget(ProjWid)
        layout=self.ui.VLayoutForMainWidget
        layout.addWidget(FrameForMainWidget)
        self.WidgetFrame=FrameForMainWidget

    def SetTasksTodayWidgetTitle(self):
        from random import choice
        date=datetime.date.today().strftime("%A %B %d %Y") if choice(range(30)) else "Doomsday"
        text=choice(("Today : ","Today is ",'Bucket list for ','Your work for ','Its already '))+ f"{date}" if choice(range(20)) else "Doomsday"  
        self.ui.CurrentWidgetTitleLabel.setText(text)
        self.ui.CurrentWidgetTitleLabel.setAlignment(QtCore.Qt.AlignCenter)

    def SetLabelForSettings(self):
        from random import choice
        text=f"App Settings" if choice(range(100)) else 'Kya re Setting ah'
        self.ui.CurrentWidgetTitleLabel.setText(text)
        self.ui.CurrentWidgetTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
    
    def SetLabelForHelp(self):
        from random import choice
        if not choice(list(range(100))):
            text=f"☝️✍️"
        else:
            text='Help Window' if choice(range(15)) else choice(("Thank you Sanjeb!","Check out discard chat app at https://github.com/sanjeb/Chat-App"))
        self.ui.CurrentWidgetTitleLabel.setText(text)
        self.ui.CurrentWidgetTitleLabel.setAlignment(QtCore.Qt.AlignCenter)


    def ShowTasksTodayWidget(self,SortOrder:int=0):
        #Deletes the current widget frame
        self.WidgetFrame.deleteLater()
        #Sets the Title
        self.SetTasksTodayWidgetTitle()
        #Show the tasks widget
        FrameForMainWidget=QtWidgets.QFrame(self.ui.MainWidgetFrame)
        framelayout=QtWidgets.QGridLayout(FrameForMainWidget)
        TaskTodayWidget=TodayTasksWidget(FrameForMainWidget,SortOrder)
        TaskTodayWidget.SortSignal.connect(lambda SortOrder: self.ShowTasksTodayWidget(SortOrder))
        framelayout.addWidget(TaskTodayWidget)
        layout=self.ui.VLayoutForMainWidget
        layout.addWidget(FrameForMainWidget)
        self.WidgetFrame=FrameForMainWidget
    
    def ShowHelpWidget(self):
        self.WidgetFrame.deleteLater()
        self.SetLabelForHelp()
        FrameForMainWidget=QtWidgets.QFrame(self.ui.MainWidgetFrame)
        framelayout=QtWidgets.QGridLayout(FrameForMainWidget)
        HelpWidg=HelpWidget(FrameForMainWidget)
        framelayout.addWidget(HelpWidg)
        layout=self.ui.VLayoutForMainWidget
        layout.addWidget(FrameForMainWidget)
        self.WidgetFrame=FrameForMainWidget
    
    def Restart(self):
        self.EXITCODE=678452056
        app=QtWidgets.QApplication.instance()
        app.exit(self.EXITCODE)
    
    def ShowSettingsWidget(self):
        #Deletes the current widget frame
        self.WidgetFrame.deleteLater()
        #Sets the Title
        self.SetLabelForSettings()
        #Show the tasks widget
        FrameForMainWidget=QtWidgets.QFrame(self.ui.MainWidgetFrame)
        framelayout=QtWidgets.QGridLayout(FrameForMainWidget)
        SettWidget=SettingsWidget(FrameForMainWidget,self)
        framelayout.addWidget(SettWidget)
        layout=self.ui.VLayoutForMainWidget
        layout.addWidget(FrameForMainWidget)
        self.WidgetFrame=FrameForMainWidget


if __name__=='__main__':
    AmberApp=QtWidgets.QApplication(sys.argv)
    win=AmberMainWindow()
    sys.exit(AmberApp.exec_())