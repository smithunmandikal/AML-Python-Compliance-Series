import pandas as pd

# 1. Use the EXACT Customer IDs found in your transactions.csv
customer_ids = ['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C007']

# 2. Create fake KYC data for them
data = {
    'Customer_ID': customer_ids,
    'Customer_Name': [
        'Alice Smith', 'Bob Jones', 'Charlie Day', 
        'Dana White', 'Eve Black', 'Frank Green', 'Grace Lee'
    ],
    'Risk_Rating': [
        'Low', 'High', 'Medium', 
        'Low', 'High', 'Medium', 'Low'
    ],
    'Country': [
        'USA', 'Canada', 'USA', 
        'UK', 'Iran', 'USA', 'China'
    ]
}

# 3. Create the dataframe and save it
df = pd.DataFrame(data)
df.to_csv('kyc_data.csv', index=False)

print("✅ Success! Corrected 'kyc_data.csv' created.")
print("You can now proceed with Day 5 merging.")