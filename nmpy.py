import pandas as pd
data = {
    'books': [2, 1, 4, 3],
    'pens': [5, 2, 6, 1]
}

index_names = ['Aarav', 'Arush', 'Bharti', 'Sneha']
df = pd.DataFrame(data, index=index_names)
print(df)