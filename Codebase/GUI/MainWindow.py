#Required Imports
import datetime
import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Codebase.Classes import classes as cl
from Codebase.GUI.UI_Classes.AmberMainWin import AmberWindowUI
from Codebase.GUI.UI_Classes.TaskWidget import TaskWidgetUI
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

        #Mainwindow Ui Setup

        #Setup of buttons
        self.ui.TasksTodayButton.clicked.connect(self.ShowTasksTodayWidget)
        self.ui.CreateProjectButton.clicked.connect(self.AddProjectButtonClicked)

        #Sets the default widget

        #Show Window
        self.show()
    
    def AddProjectButtonClicked(self):
        Title,Ok=QtWidgets.QInputDialog.getText(None,"Enter Project Name","Project Name:",)
        if Ok:
            #If the user hit 'ok', then create the project
            Proj=cl.Project(Title)
            button=QtWidgets.QPushButton(self.ui.ProjectContents)
            button.setObjectName(f"AccessProjectButton_{Proj.ID}")
            self.ui.ButtonList.addWidget(button)
            button.clicked.connect(self.ShowProjectWidget(Proj))
            
    def ShowProjectWidget(self,ProjectObj):
        self.WidgetFrame.deleteLater()
        FrameForMainWidget=QtWidgets.QFrame(self.ui.MainWidgetFrame)
        framelayout=QtWidgets.QGridLayout(FrameForMainWidget)
        framelayout.addWidget(ProjectWidget(frame=FrameForMainWidget, Project=ProjectObj))
        layout=self.ui.VLayoutForMainWidget
        layout.addWidget(FrameForMainWidget)
        self.WidgetFrame=FrameForMainWidget


    def SetTasksTodayWidgetTitle(self):
        
        date=datetime.date.today().strftime("%A %B %d %Y")
        text=f"Today : {date}" 
        self.ui.CurrentWidgetTitleLabel.setText(text)
        self.ui.CurrentWidgetTitleLabel.setAlignment(QtCore.Qt.AlignCenter)

    def ShowTasksTodayWidget(self):
        self.WidgetFrame.deleteLater()
        if self.TodaysTasksShown==False:
            self.TodaysTasksShown=True
        else:
            return
        #Sets the Title
        self.SetTasksTodayWidgetTitle()

        #Remove Everything on the WidgetFrame

        #Widget Frame is clear now

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