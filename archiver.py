import pandas as pd

df = pd.read_csv('analysis/data_cleaned/regression_data_clean.csv')
print(df.head())
df.to_csv('data/regression_data_clean.csv', index=False)