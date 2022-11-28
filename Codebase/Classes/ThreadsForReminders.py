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
        now=datetime.datetime.now()
        if now >= Date:
            ErrorLog(f"WARNING: Show Reminder called on {self.Task.ID} for an event in the past")
            return
        
        self.timediff=Date-datetime.datetime.now()
        
        #Create a daemon thread
        self.CurrentThread=threading.Thread(target=None,args=(),daemon=True)
    