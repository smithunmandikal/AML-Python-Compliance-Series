import pandas as pd
data = pd.read_csv('transactions.csv')
# FILTERING: Create a new container that ONLY has rows where Amount > 2000
high_risk = data[data['Transaction_Amount'] > 2000]
print("--- Suspicious Transactions Detected ---")
print(high_risk)

# Count how many we found
print("\nTotal Flagged:")
print(len(high_risk))
