#Required Imports
import datetime
import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from UI_Classes.AmberMainWin import AmberWindow
from UI_Classes.TasksTodayWindow import TaskTodayUI
from UI_Classes.TaskWidget import TaskWidget



class TodayTasksWidget(QtWidgets.QWidget):
    def __init__(self,frame) -> None:
        super().__init__(frame)
        self.ui=TaskTodayUI()
        self.ui.setupUi(self)
        #Sets the name of the widget
        # self.setObjectName(u"TaskTodayWidget")

class AmberMainWindow(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        
        #Sets up the mainwindow class
        super(AmberMainWindow,self).__init__()
        self.ui=AmberWindow()
        self.ui.setupUi(self)

        #Mainwindow Ui Setup

        #Sets the default widget
        self.ShowTasksTodayWidget()

        #Show Window
        self.show()
    
    def SetTasksTodayWidgetTitle(self):
        
        date=datetime.date.today().strftime("%A %B %d %Y")
        text=f"Today : {date}" 
        self.ui.CurrentWidgetTitleLabel.setText(text)
        self.ui.CurrentWidgetTitleLabel.setAlignment(QtCore.Qt.AlignCenter)

    def ShowTasksTodayWidget(self):

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
        FrameForMainWidget.setStyleSheet("background-color: #36b6b0 ;")
        

        
        





    

    
    
    
    



if __name__=='__main__':
    AmberApp=QtWidgets.QApplication(sys.argv)
    win=AmberMainWindow()
    sys.exit(AmberApp.exec_())