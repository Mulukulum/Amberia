from Codebase.Functions.Database import ExecuteCommand

Defaults=("Amberia.qss",150,250,50,0.15,1)
res=ExecuteCommand("SELECT stylesheet, mintaskdispheight, minsecdispheight, projectminheight , sidebarfactor, showhelp FROM settings WHERE def=1")
if len(res)==1:
    Settings=res[0]
else:
    Settings=Defaults
    ExecuteCommand("DELETE FROM settings")
    ExecuteCommand(f"INSERT INTO SETTINGS VALUES{(0,)+Defaults}")
    ExecuteCommand(f"INSERT INTO SETTINGS VALUES{(1,)+Defaults}")
Stylesheet,MinTaskDispHt,MinSecDispHt,ProjMinHt,sidebarfactor,HelpBehaviour=Settings
