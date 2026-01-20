import pandas as pd
# Load both datasets
transactions = pd.read_csv('transactions.csv')
kyc_data = pd.read_csv('kyc_data.csv')

print("--- Data Loaded ---")
print(f"Transactions: {len(transactions)} rows")
print(f"KYC Profiles: {len(kyc_data)} rows")

# 2. THE MERGE (The VLOOKUP replacement)
# We join them on 'Customer_ID'
# 'how=left' means: Keep all transactions, and attach KYC info where it matches
enriched_data = pd.merge(transactions, kyc_data, on='Customer_ID', how='left')

# 3. Check the result
print("\n--- Enriched Data (First 5 Rows) ---")
# Notice the new columns: Customer_Name and Risk_Rating
print(enriched_data.head())

# 4. specific check: See how many High Risk transactions we have now
high_risk_activity = enriched_data[enriched_data['Risk_Rating'] == 'High']
print("\n--- Total High Risk Transactions ---")
print(len(high_risk_activity))