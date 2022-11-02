InitSuccess=None
import Codebase.Database.Initialize as Initialize
print("Done Initialize")
if Initialize.CriticalError==True:
    InitSuccess=False
else:
    InitSuccess=True
DataBasePath=Initialize.DataBasePath
EndThread=Initialize.ThreadValue
from Codebase.Database.Functions.Connector import SignalShutDown
print('C')
import time
time.sleep(5)
SignalShutDown()
print('B')
print(EndThread)
print("Done Closing Thread")