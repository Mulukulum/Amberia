InitSuccess=None
def CheckForError():
    global InitSuccess
    import Codebase.Database.Initialize as Initialize
    if Initialize.CriticalError==True:
        InitSuccess=False
    else:
        InitSuccess=True
    return Initialize.DataBasePath
DataBasePath=CheckForError()