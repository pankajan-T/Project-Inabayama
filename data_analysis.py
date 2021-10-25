import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())
data = pd.DataFrame(2*[['detail', 'California'], ['Miami', 'Florida']])
data.to_csv('existing.csv', mode='a', index=False, header=False)