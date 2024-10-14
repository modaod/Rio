import pandas as pd
from sqlalchemy import create_engine

# Load CSV data
df = pd.read_csv('enriched.csv')

# PostgreSQL connection string
engine = create_engine('postgresql+psycopg2://riotinto:riotintopwd@localhost:5432/riotintodb')

# Write the dataframe to the PostgreSQL table
df.to_sql('enriched_data', engine, if_exists='replace', index=False)

print("Data successfully stored in PostgreSQL.")
