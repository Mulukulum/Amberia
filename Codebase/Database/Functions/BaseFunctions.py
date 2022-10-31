#The following are basic functions dealing with the database
import sqlite3

def Check(cur):
    res=cur.execute()
    return res.fetchone()