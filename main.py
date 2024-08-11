import pandas as pd

df = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')
print(df.head())
print(df.info())
print(df.describe())

df = pd.read_csv('dz.csv')
df.dropna(inplace=True)
df.to_csv('output.csv', index=False)

group = df.groupby('City')['Salary'].mean()
print(group)