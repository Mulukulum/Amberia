import sqlite3
from Codebase.Database import DataBasePath

Con=sqlite3.connect(DataBasePath)       #Creates the database file if it doesn't exist already

Con.commit()
Con.close()
