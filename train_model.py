import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("data.csv")

# Features (input)
X = data[['daily_expense', 'outings', 'food_cost', 'travel_cost']]

# Target (output)
y = data['total_expense']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")
