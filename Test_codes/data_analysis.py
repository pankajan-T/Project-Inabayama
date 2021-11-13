import pandas as pd

df = pd.read_csv('data.csv')


#print(df.iloc[0][6])
#print(df['Name'].values)
#print(df['Name'].count()) 
g=df[df["canceled time"]==1].count()[0]
print(g)