from PyQt5 import QtWidgets,QtGui,uic,QtCore
import sys

class Window(QtWidgets.QWidget):
    
    def __init__(self,Tasks:list=[]) -> None:
        super(Window,self).__init__()
        uic.loadUi('GUI//UI Files//rough.ui',self)
        for task in Tasks:
            self.AddTask(task)
        self.AddButton.clicked.connect(lambda: self.AddTask(str(self.lineEdit.text())))

    def AddTask(self,item:str) -> None:
        task=QtWidgets.QListWidgetItem(item)
        task.setFlags(task.flags()|QtCore.Qt.ItemIsUserCheckable)
        task.setCheckState(QtCore.Qt.Unchecked)
        self.tasklistwidget.addItem(task)
    


app=QtWidgets.QApplication(sys.argv)
win=Window(["Finish UI","Task 25","99.75%"])
win.show()
sys.exit(app.exec())



