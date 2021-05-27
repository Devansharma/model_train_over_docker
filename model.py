import pandas as pd
from sklearn import linear_model
import joblib

df = pd.read_csv('salary.csv')

y = df['Salary'].values.reshape(-1,1)
X = df['YearsExperience'].values.reshape(-1,1)

model = linear_model.LinearRegression()
model.fit(X, y)

joblib.dump(model, 'salary_model.pk1')
