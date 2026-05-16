import pandas as pd
import sqlite3
import os

#  Input file path
input_file =  "input.csv"

#  Ensure output folder exists
os.makedirs("output", exist_ok=True)

#  Read CSV or Excel automatically
if input_file.endswith(".csv"):
    df = pd.read_csv(input_file)
elif input_file.endswith(".xlsx"):
    df = pd.read_excel(input_file, engine="openpyxl")
else:
    raise ValueError("Unsupported file format. Use .csv or .xlsx")

print(" Raw data preview:")
print(df.head())

#  Clean data
df = df.drop_duplicates()
df = df.fillna("N/A")  # handle missing values
print(" Cleaned data:")
print(df.head())

# Transform data
df["processed"] = True
df["processed_at"] = pd.Timestamp.now()
print(" Transformed data:")
print(df.head())

# Save output file
filename = os.path.basename(input_file)
output_path = f"output/{filename}"
df.to_csv(output_path, index=False)
print(" Saved cleaned file:", output_path)

# Insert into SQLite
conn = sqlite3.connect("data.db")
df.to_sql("processed_data", conn, if_exists="append", index=False)
conn.close()
print(" Data inserted into SQLite")

# Create Excel report
report_path = f"output/report_{os.path.splitext(filename)[0]}.xlsx"
with pd.ExcelWriter(report_path) as writer:
    df.to_excel(writer, sheet_name="Processed Data", index=False)

    # Add summary sheet
    summary = df.describe(include="all")
    summary.to_excel(writer, sheet_name="Summary")

print(" Excel report created:", report_path)
