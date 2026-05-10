import pandas as pd
import mysql.connector

# Load CSV
df = pd.read_csv("../data/sensor_data.csv")

# Keep only required columns
df = df[['machine_id', 'time', 'sensor_1', 'sensor_2', 'sensor_3']]

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root123",   # 🔴 change this
    database="maintenance",
    auth_plugin='mysql_native_password'
)

cursor = conn.cursor()

# Insert data row by row
for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO sensor_readings VALUES (%s, %s, %s, %s, %s)",
        (int(row['machine_id']), int(row['time']),
         float(row['sensor_1']), float(row['sensor_2']), float(row['sensor_3']))
    )

conn.commit()

print("✅ Data inserted into MySQL!")