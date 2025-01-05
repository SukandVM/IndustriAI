import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder


data_path = '../input/preprocessed-data/preprocessed-with-no-missing.csv'

try:
    data = pd.read_csv(data_path, low_memory=False)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    raise FileNotFoundError(f"Dataset not found at {data_path}. Please check the file path.")


print("First 5 rows of the dataset:")
print(data.head())
print("\nColumns in the dataset:")
print(data.columns.tolist())

if data.empty:
    raise ValueError("The dataset is empty. Please check the file and its content.")

columns_to_drop = ['ID', 'Customer_ID', 'Name', 'SSN', 'Month']
data = data.drop(columns=[col for col in columns_to_drop if col in data.columns])

for column in data.columns:
    data[column] = pd.to_numeric(data[column], errors='coerce')

print("\nData types after conversion:")
print(data.dtypes)
print("\nMissing values per column:")
print(data.isnull().sum())

numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())

categorical_columns = [col for col in ['Occupation', 'Credit_Mix', 'Payment_of_Min_Amount', 'Payment_Behaviour'] if col in data.columns]

for column in categorical_columns:
    data[column] = data[column].fillna(data[column].mode()[0] if not data[column].isnull().all() else 'Unknown')

print("\nMissing values after filling:")
print(data.isnull().sum())

if categorical_columns:
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded_features = pd.DataFrame(encoder.fit_transform(data[categorical_columns]),
                                    columns=encoder.get_feature_names_out(categorical_columns))
    data = data.drop(columns=categorical_columns)
    data = pd.concat([data, encoded_features], axis=1)


print("\nData shape after encoding categorical variables:")
print(data.shape)


if data.isnull().sum().sum() > 0:
    print("Warning: Missing values still exist after preprocessing. Filling with median.")
    data = data.fillna(data.median())


target_column = 'Credit_Score'  
if target_column not in data.columns:
    raise ValueError(f"The target column '{target_column}' is missing from the dataset.")

features = data.drop(columns=[target_column])
target = data[target_column]


print("\nFeatures shape:", features.shape)
print("Target shape:", target.shape)


X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)


print("\nTraining set size:", X_train.shape[0])
print("Testing set size:", X_test.shape[0])

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'\nAccuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)
