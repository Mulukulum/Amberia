InitSuccess=None
import Codebase.Database.Initialize as Initialize
print("Done")
if Initialize.CriticalError==True:
    InitSuccess=False
else:
    InitSuccess=True
DataBasePath=Initialize.DataBasePath
del Initialize