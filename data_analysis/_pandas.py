import pandas as pn
from numpy.random import randn

# s1 = pn.Series([3,2,0,1])
# s2 = pn.Series([0,3,7,2])
# data = dict(apple = s1,orange=s2)
# df = pn.DataFrame(data)
# print(df)
# # print(data)

df = pn.DataFrame(randn(3,3),columns=["column1","column2","column3"],index=["a","b","c"])

# result = df[["column1","column2"]]
# result = df.loc["a"]
# result = df.loc[:,["column1","column3"]]
# result = df.loc[:"b","column1":"column3"]
# result = df.loc[["a","b"],["column1","column3"]]
# result = df.loc[["a","b"],"column1":"column3"]
df ["column4"] = pn.Series(randn(3),["a","b","c"])




print(df)
# print(result)