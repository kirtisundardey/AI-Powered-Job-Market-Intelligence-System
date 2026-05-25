import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv('data/processed/cleaned_jobs.csv')

# Encode categorical columns
le = LabelEncoder()

categorical_cols = [
    'Job_Title_Sim',
    'Job_City',
    'Industry'
]

for col in categorical_cols:
    df[col] = le.fit_transform(df[col].astype(str))

print(df.head())