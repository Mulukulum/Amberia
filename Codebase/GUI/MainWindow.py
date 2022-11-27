#Required Imports
import datetime
import sys
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui

from UI_Files.AmberMainWin import AmberWindow

class AmberMainWindow(PyQt5.QtWidgets.QMainWindow):

    def __init__(self) -> None:
        
        #Sets up the mainwindow class
        super(AmberMainWindow,self).__init__()
        self.ui=AmberWindow()
        self.ui.setupUi(self)

        #Mainwindow Ui Setup

        #Sets the current Date
        self.SetTasksTodayWidgetTitle()

        #Show Window
        self.show()
    
    def SetTasksTodayWidgetTitle(self):
        
        date=datetime.date.today().strftime("%A %B %d %Y")
        text=f"Today : {date}" 
        self.ui.CurrentWidgetTitleLabel.setText(text)
        self.ui.CurrentWidgetTitleLabel.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
    
    


if __name__=='__main__':
    AmberApp=PyQt5.QtWidgets.QApplication(sys.argv)
    win=AmberMainWindow()
    sys.exit(AmberApp.exec_())