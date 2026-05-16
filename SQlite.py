import sqlite3

conn=sqlite3.connect("test.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    age INTEGER,
    city TEXT
)
""")
conn.commit()
conn.close()

conn=sqlite3.connect("test.db")
cursor=conn.cursor()

cursor.execute("INSERT INTO users VALUES('john',25,'Delhi')")
cursor.execute("INSERT INTO users VALUES('sarah',30,'Mumbai') ")

conn.commit()
conn.close()

import pandas as pd
import sqlite3

conn=sqlite3.connect("test.db")
df=pd.read_sql("SELECT*FROM users",conn)
print(df)

conn.close()

df=pd.read_csv("input.csv")

conn=sqlite3.connect("test.db")
df.to_sql("user",conn,if_exists="replace",
index=False)

conn.close()