import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load dataset
df = pd.read_csv('data/processed/cleaned_jobs.csv')

# Select features
X = df[
    [
        'Rating',
        'Company_Age',
        'Python',
        'SQL',
        'AWS',
        'Spark',
        'Excel'
    ]
]

# Target column
y = df['Salary_Avg']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("MAE:", mae)
print("R2 Score:", r2)

# Save model
joblib.dump(model, 'salary_model.pkl')

print("Model saved successfully!")