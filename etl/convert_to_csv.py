import pandas as pd

# Step 1: Load file
file_path = "..//data//train_FD001.txt"

df = pd.read_csv(file_path, sep=" ", header=None)

# Step 2: Remove empty columns
df = df.dropna(axis=1)

# Step 3: Rename columns
num_cols = df.shape[1]

columns = ["machine_id", "time"] + [f"sensor_{i}" for i in range(1, num_cols-1)]
df.columns = columns

# Step 4: Save CSV
df.to_csv("../data/sensor_data.csv", index=False)

print("✅ CSV created successfully!")