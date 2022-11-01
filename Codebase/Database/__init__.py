InitSuccess=None
import Codebase.Database.Initialize as Initialize
if Initialize.CriticalError==True:
    InitSuccess=False
else:
    InitSuccess=True
DataBasePath=Initialize.DataBasePath
del Initialize