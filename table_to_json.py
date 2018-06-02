import pandas as pd

df = pd.read_csv('table.csv')
print(df.to_json(orient='index'))
