import sqlite3
from sqlite3 import Error
database = r".\data\pythondb.db"
 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn