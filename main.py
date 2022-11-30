import pandas as pd

#1
df = pd.read_csv('regression_data.csv')
print(df.info())

#2
df.drop(['date'], axis=1, inplace=True)
print(df.head(10))
