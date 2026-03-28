import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

print("Enter your details:")

daily = float(input("Daily expense: "))
outings = int(input("Outings: "))
food = float(input("Food cost: "))
travel = float(input("Travel cost: "))

# Create DataFrame with column names
input_data = pd.DataFrame([[daily, outings, food, travel]],
                          columns=['daily_expense', 'outings', 'food_cost', 'travel_cost'])

# Predict
result = model.predict(input_data)

print("\nEstimated Monthly Expense: ₹", int(result[0]))