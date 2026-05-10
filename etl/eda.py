import pandas as pd

# Load dataset
df = pd.read_csv("../data/sensor_data.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Show shape (rows, columns)
print("\nShape of data:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic statistics
print("\nSummary statistics:")
print(df.describe())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values (if any)
df = df.ffill()

print("\nAfter cleaning:")
print(df.shape)

# Average sensor values per machine
avg_sensor = df.groupby("machine_id")["sensor_1"].mean()

print("\nAverage sensor_1 per machine:")
print(avg_sensor.head())