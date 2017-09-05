import pandas as pd

name='csv/sum.csv'
data=pd.read_csv(name)
print(data)
# print(data[0])
print(data.mean())