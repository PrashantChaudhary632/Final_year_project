import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("D:/Final Year Project/wtvtable.csv")
df.head()

print(df.columns)

X = df[['P', 'S']]
Y = df['W']
# print(X)

print("Coefficient: ",model.coef_)

wtv= model.predict([[30,2500]])
print(wtv)