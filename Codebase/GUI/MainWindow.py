#Required Imports
import datetime
import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

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

        #Mainwindow Ui Setup

        #Setup of buttons
        self.ui.TasksTodayButton.clicked.connect(self.ShowTasksTodayWidget)
        self.ui.CreateProjectButton.clicked.connect(lambda: print(5))

        #Sets the default widget

        #Show Window
        self.show()
    
    def AddProject(self):
        ...

    def SetTasksTodayWidgetTitle(self):
        
        date=datetime.date.today().strftime("%A %B %d %Y")
        text=f"Today : {date}" 
        self.ui.CurrentWidgetTitleLabel.setText(text)
        self.ui.CurrentWidgetTitleLabel.setAlignment(QtCore.Qt.AlignCenter)

    def ShowTasksTodayWidget(self):

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


if __name__=='__main__':
    AmberApp=QtWidgets.QApplication(sys.argv)
    win=AmberMainWindow()
    sys.exit(AmberApp.exec_())