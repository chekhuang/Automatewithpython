import pandas as pd

#sample data
data = {
    "Name": [
        "Alice Johnson", "Michael Smith", "Sara Lee", "David Kumar",
        "Priya Sharma", "John Doe", "Emily Brown", "Ravi Patel",
        "Sophia Wilson", "Arun Gupta"
    ],
    "Age": [28, 35, 30, 40, 25, 32, 29, 38, 27, 45],
    "Salary (₹)": [45000, 60000, 52000, 70000, 40000, 55000, 48000, 65000, 47000, 80000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("input.xlsx", index=False, engine="openpyxl")

print("Excel file 'input.xlsx' created successfully!")

import pandas as pd

import pandas as pd

# Read Excel
df = pd.read_excel("input.xlsx", engine="openpyxl")

print("Original data:")
print(df)

# Process: calculate summary statistics
avg_salary = df["Salary (₹)"].mean()
min_salary = df["Salary (₹)"].min()
max_salary = df["Salary (₹)"].max()
median_salary = df["Salary (₹)"].median()
avg_age = df["Age"].mean()
min_age = df["Age"].min()
max_age = df["Age"].max()

# Top 5 earners
top5 = df.sort_values(by="Salary (₹)", ascending=False).head(5)

# Write output
with pd.ExcelWriter("output.xlsx", engine="openpyxl") as writer:
    # Raw data
    df.to_excel(writer, sheet_name="Raw", index=False)

    # Summary sheet
    summary = pd.DataFrame({
        "Metric": [
            "Average Salary", "Minimum Salary", "Maximum Salary", "Median Salary",
            "Average Age", "Minimum Age", "Maximum Age"
        ],
        "Value": [
            avg_salary, min_salary, max_salary, median_salary,
            avg_age, min_age, max_age
        ]
    })
    summary.to_excel(writer, sheet_name="Summary", index=False)

    # Top 5 earners sheet
    top5.to_excel(writer, sheet_name="Top5Earners", index=False)

print("Report generated successfully!")
