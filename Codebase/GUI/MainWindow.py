#Required Imports

import sys
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui

from UI_Files.AmberMainWin import AmberWindow

class AmberMainWindow(PyQt5.QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui=AmberWindow()
        self.ui.setupUi(self)
        self.show()
    
    def SetCurrentDate():
        ...

if __name__=='__main__':
    AmberApp=PyQt5.QtWidgets.QApplication(sys.argv)
    win=AmberMainWindow()
    sys.exit(AmberApp.exec_())