import pandas as pd

# Load dataset
data = pd.read_csv("students.csv")

print("First 5 Rows:")
print(data.head())

print("\nShape:")
print(data.shape)

print("\nColumns:")
print(data.columns)

print("\nSummary:")
print(data.describe())

print("\nMissing Values:")
print(data.isnull().sum())