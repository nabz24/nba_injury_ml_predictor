import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your dataset
df = pd.read_csv("database_24_25.csv")

# Create fake label if needed (for demo)
import numpy as np
df['isInjuredNextGame'] = np.random.choice([0, 1], size=len(df), p=[0.8, 0.2])

# Select features and label
X = df[['MP', 'FGA', 'TRB', 'AST', 'PF', 'PTS']].fillna(0)
y = df['isInjuredNextGame']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model to pickle file
with open("nba_model.pkl", "wb") as f:
    pickle.dump(model, f)