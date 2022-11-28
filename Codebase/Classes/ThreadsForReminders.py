#This File contains functionality for the threads of the tasks

import threading
import datetime
import concurrent.futures as cf
import Codebase.Classes.classes as cl
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Codebase.ErrorLogs.logging import ErrorLog

class EmitNotificationThread(QtCore.QObject):
    


    def __init__(self) -> None:
        pass

    @QtCore.pyqtSlot(datetime.datetime)
    def StartThread(self,Date: datetime.datetime):
        #If the date is less than the current time then just return
        if Date<=datetime.datetime.now():
            ErrorLog
            return
        ...

def main():
    ...