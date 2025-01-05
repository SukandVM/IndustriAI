import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans

data = pd.read_csv('/kaggle/input/financial-habits-dataset/financial_habits_survey01.csv') 

print(data.head()) 
print(data.describe()) 

data = pd.get_dummies(data, columns=['Education'], drop_first=True)  

data = data.dropna()  

X = data.drop('Spending Habits', axis=1) 
y = data['Spending Habits']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

plt.scatter(y_test, y_pred)
plt.xlabel('Actual Spending Habits')
plt.ylabel('Predicted Spending Habits')
plt.title('Actual vs Predicted Spending Habits')
plt.show()

kmeans = KMeans(n_clusters=3) 
data['Cluster'] = kmeans.fit_predict(X)

plt.scatter(data['Income'], data['Credit Score'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Income')
plt.ylabel('Credit Score')
plt.title('Clusters of Financial Habits')
plt.show()
