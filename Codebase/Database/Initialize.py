import sqlite3
from Codebase.Database import DataBasePath      #Gets the path of the database on the machine
from Codebase.Database.Functions.StartUp import Check
Con=sqlite3.connect(DataBasePath)       #Creates the database file if it doesn't exist already and makes a connection
Cursor=Con.cursor()

Con.commit()
Con.close()