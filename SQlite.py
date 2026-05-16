import sqlite3
import pandas as pd

conn = sqlite3.connect("./data/test.db")
cursor = conn.cursor()

def CreateTb():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)
    conn.commit()
    conn.close()

def InsertData():
    conn = sqlite3.connect("./data/test.db")
    cursor=conn.cursor()

    cursor.execute("INSERT INTO users VALUES('CK',25,'Delhi')")
    cursor.execute("INSERT INTO users VALUES('KA',30,'Mumbai') ")

    conn.commit()
    conn.close()

def ReadData():

    conn=sqlite3.connect("./data/test.db")
    df=pd.read_sql("SELECT * FROM users",conn)
    conn.close()
    print(df)

CreateTb()
InsertData()
ReadData()

