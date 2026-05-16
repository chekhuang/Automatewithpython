import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # endpoint for a single post
response = requests.get(url)

print("Status code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Raw text:", response.text)

# Only parse JSON if valid
if response.headers.get("Content-Type") == "application/json; charset=utf-8":
    data = response.json()
    print(data)
else:
    print("Not JSON:", response.text)


import pandas as pd

df = pd.DataFrame([data])

print(df.head())

df.to_csv("api_data.input.csv", index=False)

filtered=df[df["userId"]==1]
print(filtered)

import sqlite3

conn=sqlite3.connect("test.db")
df.to_sql("api_posts",conn,if_exists="replace",
index=False)
conn.close()








