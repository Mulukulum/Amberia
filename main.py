####################################     PROGRESS     ####################################

# The backend is now nearly done, with only tasks left to clean up
# As for the UI, Widgets for pretty much everything are almost done, only thing left is 
# to add each widget to QScrollArea, QHBoxLayout and QVBoxLayouts and UI will be finished
# Functions for connecting the backend to the ui haven't had any work started on them

from PyQt5 import QtWidgets
#To pass in sys.argv to the app
import sys
#Setup the Classes, this also sets up the database
from Codebase.Classes import classes as cl
#To run the GUI
from Codebase.GUI.MainWindow import AmberMainWindow
#To retrieve data from a save, this file retrieves everything
from Codebase.Classes import RetrieveFromDB

AmberApp=QtWidgets.QApplication(sys.argv)
win=AmberMainWindow()
sys.exit(AmberApp.exec_())


# Also rohit if you're reading this I couldn't do the UI stuff yet, sorry
# I'll work on them tonight and this'll mostly be done by this saturday
# which leaves 2 days for fixing bugs and adding any last minute features
