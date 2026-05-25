from sqlalchemy import create_engine
import pandas as pd

# Create database
engine = create_engine('sqlite:///jobs.db')

# Load dataset
df = pd.read_csv('data/processed/cleaned_jobs.csv')

# Insert into SQL
df.to_sql(
    'jobs',
    engine,
    if_exists='replace',
    index=False
)

print('Data inserted successfully!')