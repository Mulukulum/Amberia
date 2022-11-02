from os import getpid
if getpid():
    InitSuccess=None
    import Codebase.Database.Initialize as Initialize
    if Initialize.CriticalError==True:
        InitSuccess=False
    else:
        InitSuccess=True
    DataBasePath=Initialize.DataBasePath
    #EndProcess=Initialize.ProcessValue
    #print(EndProcess,'hi')
    del getpid