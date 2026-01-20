import pandas as pd
# 1. Re-create our merged dataset (copying logic from Day 5)
transactions = pd.read_csv('transactions.csv')
kyc_data = pd.read_csv('kyc_data.csv')
enriched_data = pd.merge(transactions, kyc_data, on='Customer_ID', how='left')
# 2. Create a Final Report View
# Let's say we only want High Risk customers with amounts > $2000
final_report = enriched_data[
    (enriched_data['Risk_Rating'] == 'High')&
(enriched_data['Transaction_Amount'] > 2000)
]
print("Generatng Excel report...")

# 3. EXPORT TO EXCEL
# 'index=False' means we don't print the row numbers (0, 1, 2...)
final_report.to_excel("Suspicious_Activity_Report.xlsx", index=False)
print("Success! File 'Suspicious_Activity_Report.xlsx' has been created.")