import pandas as pd
data = pd.read_csv('transactions.csv')
print("--- Checking the first 5 rows ---")
print(data.head())
# Group by Customer and Sum the amounts
risk_summary = data.groupby('Customer_ID')['Transaction_Amount'].sum()

print("\n--- Total Volume per Customer ---")
print(risk_summary)
