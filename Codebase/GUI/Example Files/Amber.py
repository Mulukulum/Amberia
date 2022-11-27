import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import datetime



from MainWindow import Ui_MainWindow as AmberWindowUI

from TaskDisplay import Ui_Form as TaskDispUI

class AmberApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super(AmberApplicationWindow,self).__init__()
        self.ui=AmberWindowUI()
        self.ui.setupUi(self)
        self.ui.date_label.setText(f"{datetime.date.today().strftime('%A, %B %d %Y')}")
        self.ui.vert=QtWidgets.QVBoxLayout(self.ui.WidgetFrame)
        self.ui.vert.setObjectName(u"Layout for Widget")
        self.ui.tasks_today_button.clicked.connect(self.ToggleTask)
        self.AddTask()
        self.Active=True
        

    def AddTask(self):
        frame=QtWidgets.QFrame(self.ui.WidgetFrame)
        frame.setObjectName(u"uniqueid")
        framelayout=QtWidgets.QVBoxLayout(frame)
        framelayout.addWidget(TaskDisplayWidget())
        frame.setStyleSheet("background-color: #36b6b0 ;")

        layout= self.ui.vert    

        layout.addWidget(frame)
        self.Active=True

    def RemoveTask(self):
        frame=self.ui.WidgetFrame.findChild(QtWidgets.QFrame,u"uniqueid")
        frame.deleteLater()
        self.Active=False
    
    def ToggleTask(self):
        if self.Active:
            self.RemoveTask()
        else:
            self.AddTask()


        




class TaskDisplayWidget(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()
        ui=TaskDispUI()
        ui.setupUi(self)
        

app=QtWidgets.QApplication(sys.argv)
win=AmberApplicationWindow()
win.show()
sys.exit(app.exec_())

    





