from PyQt5 import QtWidgets
#To pass in sys.argv to the app
import importlib
from Codebase.Functions import Database
import sys
#Setup the Classes, this also sets up the database
from Codebase.Classes import classes as cl
#To run the GUI
from Codebase.GUI.MainWindow import AmberMainWindow
#To retrieve data from a save, this file retrieves everything
from Codebase.Classes import RetrieveFromDB
import Codebase.GUI.MainWindow
import Codebase.GUI.Widgets
import Codebase.GUI.UserSettings

code=678452056
while code:
    AmberApp=QtWidgets.QApplication(sys.argv)
    win=AmberMainWindow()
    code=AmberApp.exec_()
    #REQUIRED LINE DO NOT REMOVE THIS
    del AmberApp
    #If the application needs to restart
    if code:
        importlib.invalidate_caches()
        importlib.reload(Codebase.GUI.UserSettings)
        importlib.reload(Codebase.GUI.Widgets)
        importlib.reload(Codebase.GUI.MainWindow)

Database.CloseConnection()
