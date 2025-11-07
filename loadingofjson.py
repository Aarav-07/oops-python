import pandas as pd

df = pd.read_json('stationery_sales.json', orient='index')
print(df)
