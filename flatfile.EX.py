import pandas as pd

#read file
df=pd.read_csv("input.input.csv")

print("original data:")
print(df)

#clean data
df['name']=df["name"].str.strip().str.lower()
df["city"]=df["city"].str.strip()

#fill missing ages
df["age"]=df["age"].fillna(0)

#transform
def categorize(age):
    return"young"if age<30 else "adult"
df["category"]=df["age"].apply(categorize)

#save
df.to_csv("output.input.csv",index=False)

print("cleaned data:")
print(df)