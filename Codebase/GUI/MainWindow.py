#Required Imports
import datetime
import sys
import os.path
import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Codebase.Functions.Colors import HexFormat
from Codebase.Classes import classes as cl
from Codebase.GUI.UI_Classes.AmberMainWin import AmberWindowUI
from Codebase.GUI.Widgets import (
    TodayTasksWidget, ProjectWidget
    )


class AmberMainWindow(QtWidgets.QMainWindow):


    def __init__(self) -> None:
        
        #Sets up the mainwindow class
        super(AmberMainWindow,self).__init__()
        self.ui=AmberWindowUI()
        self.ui.setupUi(self)
        self.TodaysTasksShown=False
        self.WidgetFrame=QtWidgets.QFrame()
        self.setWindowIcon(QtGui.QIcon(os.path.dirname(__file__)+r"\\UI_Files\\Icon.png"))
        self.setWindowTitle("Amberia")
        #Mainwindow Ui Setup
        #Color Setup
        with open(os.path.dirname(__file__)+r"\\StyleSheet\\Amberia.qss") as f:
            self.setStyleSheet(f.read())
        #self.setStyleSheet("background-color : #1c1d21 ;")
        
        #Set the Shortcuts for the Buttons
        self.ui.TasksTodayButton.setShortcut("ctrl+h")
        self.ui.CreateProjectButton.setShortcut("ctrl+n")

        #Set the connections of the buttons
        self.ui.TasksTodayButton.clicked.connect(self.ShowTasksTodayWidget)
        self.ui.CreateProjectButton.clicked.connect(self.AddProjectButtonClicked)

        #Sets the default widget
        self.ShowTasksTodayWidget()
        #Makes the buttons for the existing projects
        self.RetrieveFromDB()
        #Show Window
        self.show()
    
    def RemoveProjectButton(self,ObjectName: str):
        button=self.findChildren(QtWidgets.QPushButton,ObjectName)[0]
        button.deleteLater()
        self.ShowTasksTodayWidget()
        self.ui.TasksTodayButton.click()
    
    def RetrieveFromDB(self):
        #Function to update the UI with project buttons
        for Project in cl.Project.Instances.values():
            self._AddProjectFromDB(Project)
    
    def _AddProjectFromDB(self,Proj: cl.Project):
        button=QtWidgets.QPushButton(self.ui.ProjectContents)
        button.setObjectName(f"AccessProjectButton_{Proj.ID}")
        button.setText(Proj.Title)
        button.setStyleSheet(f"background-color: {HexFormat(Proj.Color)} ; ")
        self.ui.ButtonList.addWidget(button)
        button.clicked.connect(lambda: self.ShowProjectWidget(Proj))

    def AddProjectButtonClicked(self):
        #Popup the dialog
        Dialog=QtWidgets.QInputDialog(None)
        Title,Ok=Dialog.getText(self,"Add Project","Project Name:",)
        if Ok:
            #If the user hit 'ok', then create the project
            #If the input is empty, then do nothing
            if not Title.strip(): return
            Title=Title.lstrip('_')
            Proj=cl.Project(Title)
            button=QtWidgets.QPushButton(self.ui.ProjectContents)
            button.setObjectName(f"AccessProjectButton_{Proj.ID}")
            button.setText(Proj.Title)
            button.setStyleSheet(f"background-color: {HexFormat(Proj.Color)} ; ")
            self.ui.ButtonList.addWidget(button)
            button.clicked.connect(lambda: self.ShowProjectWidget(Proj))
            button.click()
            
    def ShowProjectWidget(self,ProjectObj):
        #Delete the current Widget that is shown and add the other widget after creating it
        self.WidgetFrame.deleteLater()
        FrameForMainWidget=QtWidgets.QFrame(self.ui.MainWidgetFrame)
        framelayout=QtWidgets.QGridLayout()
        #Connect the signals and slots
        ProjWid=ProjectWidget(frame=FrameForMainWidget, Project=ProjectObj)
        ProjWid.SignalDeleteProjectButton.connect(lambda objname: self.RemoveProjectButton(objname))

        framelayout.addWidget(ProjWid)
        layout=self.ui.VLayoutForMainWidget
        layout.addWidget(FrameForMainWidget)
        self.WidgetFrame=FrameForMainWidget

    def SetTasksTodayWidgetTitle(self):
        
        date=datetime.date.today().strftime("%A %B %d %Y")
        text=f"Today : {date}" 
        self.ui.CurrentWidgetTitleLabel.setText(text)
        self.ui.CurrentWidgetTitleLabel.setAlignment(QtCore.Qt.AlignCenter)

    def ShowTasksTodayWidget(self):
        
        #Deletes the current widget frame
        self.WidgetFrame.deleteLater()
        #Sets the Title
        self.SetTasksTodayWidgetTitle()
        #Show the tasks widget
        FrameForMainWidget=QtWidgets.QFrame(self.ui.MainWidgetFrame)
        framelayout=QtWidgets.QGridLayout(FrameForMainWidget)
        framelayout.addWidget(TodayTasksWidget(FrameForMainWidget))
        layout=self.ui.VLayoutForMainWidget
        layout.addWidget(FrameForMainWidget)
        self.WidgetFrame=FrameForMainWidget
        

if __name__=='__main__':
    AmberApp=QtWidgets.QApplication(sys.argv)
    win=AmberMainWindow()
    sys.exit(AmberApp.exec_())