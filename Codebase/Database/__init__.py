InitSuccess=None
import Codebase.Database.Initialize as Initialize
if Initialize.CriticalError==True:
    InitSuccess=False
else:
    InitSuccess=True
DataBasePath=Initialize.DataBasePath
EndProcess=Initialize.ProcessValue
print(EndProcess,'hi')
'''
print(EndProcess,'is the process')
from Codebase.Database.Functions.Connector import SignalShutDown
from time import sleep
sleep(10)
print(f"{EndProcess} is process now ShutDown")
SignalShutDown()
print(f"{EndProcess} is process now")
print('ShutDown')
'''