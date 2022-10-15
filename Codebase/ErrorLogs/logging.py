#Functions to log errors with other functions

from os.path import dirname

LogPath=(dirname(__file__).partition("Codebase")[0])+("LogFiles\\")         #Gets the path of the logs Folder

def CreateLog(text=None,FileName=__file__):
    return FileName,text    