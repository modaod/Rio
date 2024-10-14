import pandas as pd

# Load the CSV file
df = pd.read_csv('pace-data.txt')

# Normalize MovementDateTime to ISO format
df['MovementDateTime'] = pd.to_datetime(df['MovementDateTime']).dt.strftime('%Y-%m-%dT%H:%M:%S')

# Identify rows where MoveStatus is "Under way using engine" and Speed is either zero or missing
missing_speed = (df['MoveStatus'] == "Under way using engine") & ((df['Speed'] == 0) | (df['Speed'].isna()))

# Assign the average speed for the corresponding CallSign
df.loc[missing_speed, 'Speed'] = df.loc[missing_speed, 'CallSign'].map(
    df[df['MoveStatus'] == "Under way using engine"].groupby('CallSign')['Speed'].mean()
)

# BeamRatio feature 
df['BeamRatio'] = df['Beam'] / df['Length']

# Save data into a CSV file
df.to_csv('enriched.csv', index=False)

print("Data saved to enriched.csv")
