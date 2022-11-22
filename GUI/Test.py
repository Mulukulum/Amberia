from PyQt5 import QtWidgets,QtCore,QtGui,uic
import sys

class Window(QtWidgets.QWidget):
    
    def __init__(self) -> None:
        super(Window,self).__init__()
        uic.loadUi('rough.ui',self)

app=QtWidgets.QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec())



