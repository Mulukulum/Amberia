import sqlite3
from Codebase.Database import DataBasePath
from Codebase.Database.Functions.BaseFunctions import Check
Con=sqlite3.connect(DataBasePath)       #Creates the database file if it doesn't exist already
Cursor=Con.cursor()
print(Check(Cursor))
Con.commit()
Con.close()
