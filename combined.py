import pandas as pd

social_data = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104],
    'PostID': [1, 2, 3, 4],
    'Text': ['I pay all my bills on time', 'I missed my utility payment', 
             'I am struggling to save money', 'Financial stability is key'],
    'Sentiment': ['Positive', 'Negative', 'Negative', 'Positive']
})

utility_data = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104],
    'Month': ['January', 'January', 'February', 'February'],
    'PaymentStatus': ['Paid', 'Missed', 'Paid', 'Missed']
})

geo_data = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104],
    'City': ['New York', 'Los Angeles', 'San Francisco', 'Miami'],
    'StabilityScore': ['High', 'Low', 'Medium', 'Low']
})

social_data['Sentiment'].fillna('Unknown', inplace=True)
social_data.drop_duplicates(inplace=True)

utility_data['PaymentStatus'].fillna('Unknown', inplace=True)
utility_data.drop_duplicates(inplace=True)

geo_data['StabilityScore'].fillna('Unknown', inplace=True)
geo_data.drop_duplicates(inplace=True)

merged_data = pd.merge(social_data, utility_data, on="CustomerID", how="inner")
merged_data = pd.merge(merged_data, geo_data, on="CustomerID", how="inner")

merged_data.to_csv("final_merged_data.csv", index=False)

print("Data collection and integration completed successfully!")
print(merged_data)
