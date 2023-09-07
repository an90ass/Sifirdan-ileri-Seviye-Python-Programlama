import pandas as pn
import numpy as np


data = np.random.randint(10,100,15).reshape(5,3)
df = pn.DataFrame(data,index=['a','c','e','f','h'],columns=["column1","column2","column3"])
result = df
df =df.reindex(['a','b','c','d','e','f','g','h'])
new_column = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"]=new_column
result = df
result = df.drop("column1",axis=1)

result = df.drop(["column1","column3"],axis=1).drop("a",axis=0)

result = df.isnull()
result =df[df["column1"].isnull()]
result =df[df["column1"].isnull()]["column1"]
result =df[df["column1"].notnull()]["column1"]
result = df.dropna()
result = df.dropna(axis=1)#sutun bir nan varsa o sutuna gitirilmez

result = df.dropna(axis=1,how = "all")
result = df.dropna(how = "all")

result = df.dropna(subset  = ["column1","column2"], how = "all")
result = df.dropna(subset  = ["column1","column2"], how = "any")
result = df.dropna(thresh = 2)
result = df.dropna(thresh = 3) # en az sayıda normal veri

result = df.fillna(value = 'no input')
result = df.fillna(value = 1)

result = df.sum()
result = df.sum().sum()
result = df.size
result = df.isnull().sum()
result = df.isnull().sum().sum()

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

result = df.fillna(value = ortalama(df))
print(result)