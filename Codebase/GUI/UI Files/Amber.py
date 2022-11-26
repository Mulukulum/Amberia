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
        

    def ShowTaskWidget(self,Widget):
        self.ui.vertical.addWidget(Widget)
        self.show()



class TaskDisplayWidget(QtWidgets.QWidget):

    def __init__(self,MainWindow: AmberApplicationWindow) -> None:
        super().__init__(MainWindow.ui.scrollAreaWidgetContents_2)
        ui=TaskDispUI()
        ui.setupUi(MainWindow)
        

app=QtWidgets.QApplication(sys.argv)
win=AmberApplicationWindow()
win.ShowTaskWidget(TaskDisplayWidget(win))
win.show()
sys.exit(app.exec_())

    





