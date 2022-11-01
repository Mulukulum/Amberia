InitSuccess=None
def CheckForError():
    global InitSuccess
    import Codebase.Database.Initialize as Initialize
    if Initialize.CriticalError==True:
        
        InitSuccess=False
    else:
        print('3',Initialize.CriticalError)
        InitSuccess=True
    return Initialize.GetPathDatabase()
DataBasePath=CheckForError()
print('1',DataBasePath)
print('2',InitSuccess)
