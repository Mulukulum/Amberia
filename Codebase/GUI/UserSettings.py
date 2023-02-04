from Codebase.Functions.Database import ExecuteCommand

Defaults=("Amberia.qss",275,400,65,0.235,1)
res=ExecuteCommand("SELECT stylesheet, mintaskdispheight, minsecdispheight, projectminheight , sidebarfactor, showhelp FROM settings WHERE def=1")
if len(res)==1:
    Settings=res[0]
else:
    Settings=Defaults
    ExecuteCommand("DELETE FROM settings")
    ExecuteCommand("INSERT INTO SETTINGS VALUES(0,'Amberia.qss',275,400,65,0.235,1)")
    ExecuteCommand("INSERT INTO SETTINGS VALUES(1,'Amberia.qss',275,400,65,0.235,1)")
Stylesheet,MinTaskDispHt,MinSecDispHt,ProjMinHt,sidebarfactor,HelpBehaviour=Settings
