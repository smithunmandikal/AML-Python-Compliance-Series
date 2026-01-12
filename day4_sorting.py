import pandas as pd

# Load data
data = pd.read_csv('transactions.csv')

# Create the profile (Sum and Count)
profile = data.groupby('Customer_ID')['Transaction_Amount'].agg(['sum', 'count'])
# Sort the profile so the highest volume customers are at the top
top_risks = profile.sort_values(by='sum', ascending=False)
print("--- Top 5 Highest Risk Customers ---")
print(top_risks.head(5))