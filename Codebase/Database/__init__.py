InitSuccess=None
import Codebase.Database.Initialize as Initialize
print("Done Initialize")
if Initialize.CriticalError==True:
    InitSuccess=False
else:
    InitSuccess=True
print("H")
DataBasePath=Initialize.DataBasePath
print("D")
EndThread=Initialize.ThreadValue
print('A')
from Codebase.Database.Functions.Connector import SignalShutDown,ShutDownRequest
print('C')
print(ShutDownRequest)
SignalShutDown()
print(ShutDownRequest)
print('B')
EndThread.join()
print("Done Closing Thread")