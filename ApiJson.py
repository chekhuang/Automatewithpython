import requests
import pandas as pd
import os
# import requests
# import pandas as pd
# import requests
# import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
data = requests.get(url).json()

df = pd.json_normalize(data)

# Select only city and company name
subset = df[["address.city", "company.name"]]

# Rename columns to simpler names
subset = subset.rename(columns={
    "address.city": "City",
    "company.name": "Company"
})

print(subset.head())
df.to_csv("output/users.csv", index=False)

url = "https://randomuser.me/api/?results=5"
data = requests.get(url).json()

results = data["results"]

df = pd.json_normalize(results)

#select only name and email

print(df[["name.first", "email"]])

all_data = []

for i in range(1, 4):  # pages
    url = f"https://jsonplaceholder.typicode.com/posts?_page={i}"
    data = requests.get(url).json()
    all_data.extend(data)

df=pd.DataFrame(all_data)
print("\nFirst 5 rows:")
print (df.head)
df = pd.DataFrame(all_data)
print(df.shape)
