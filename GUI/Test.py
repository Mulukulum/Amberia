import PyQt5.QtWidgets
import PyQt5.QtGui
import sys

def Window():
    app=PyQt5.QtWidgets.QApplication(sys.argv)
    win=PyQt5.QtWidgets.QMainWindow()    
    win.setGeometry(960,540,400,400)
    win.setWindowIcon(PyQt5.QtGui.QIcon(r'H:\\4. Computer Science\\ProjectClass12\\Mike-Romeo\\GUI\\Assets\\treeman.png'))
    win.setWindowTitle("Amber")
    label= PyQt5.QtWidgets.QLabel(win)
    label.setText("Hi Mom!")
    label.move(200,200)
    win.show()
    app.exec()
Window()

