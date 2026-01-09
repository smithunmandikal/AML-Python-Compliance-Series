import pandas as pd
data = pd.read_csv('transactions.csv')
# Group by Customer, and calculate specific metrics for the 'Transaction_Amount'
# We want the 'sum' (Total Volume) AND 'count' (Frequency)
risk_profile = data.groupby('Customer_ID')['Transaction_Amount'].agg(['sum', 'count'])
# Rename the columns to make them readable
risk_profile.columns = ['Total_Volume', 'Transaction_Count']

# Sort by Count to see the most frequent transactors first
structuring_suspects = risk_profile.sort_values(by='Transaction_Count', ascending=False)

print("--- Potential Structuring Suspects ---")
print(structuring_suspects.head())

