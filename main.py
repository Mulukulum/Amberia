from PyQt5 import QtWidgets
#To pass in sys.argv to the app
import sys
#Setup the Classes, this also sets up the database
from Codebase.Classes import classes as cl
#To run the GUI
from Codebase.GUI.MainWindow import AmberMainWindow
#To retrieve data from a save, this file retrieves everything
from Codebase.Classes import RetrieveFromDB
from Codebase.Functions import Database

AmberApp=QtWidgets.QApplication(sys.argv)
win=AmberMainWindow()
code=AmberApp.exec_()

Database.CloseConnection()
sys.exit(code)
