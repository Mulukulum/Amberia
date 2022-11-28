#This File contains functionality for the threads of the tasks

import threading
import datetime
import concurrent.futures as cf
import Codebase.Classes.classes as cl
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Codebase.ErrorLogs.logging import ErrorLog

class NotificationThread:
    
    def __init__(self,Task: cl.Task) -> None:
        self.Task=Task
        self.Stop=threading.Event()


    def ShowReminder(self,Date: datetime.datetime):
        #If the date is less than the current time then just return
        if Date<=datetime.datetime.now():
            ErrorLog("WARNING: Show Reminder called without Initialisation of ")
            return
        #Create a daemon thread
        self.CurrentThread=threading.Thread(target=None,args=(),daemon=True)
    

def main():
    ...