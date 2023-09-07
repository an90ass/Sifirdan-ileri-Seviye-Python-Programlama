import pandas as pn
data = pn.read_csv("datasets/imdb.csv")
result = data
result = pn.DataFrame(data)
result = data.head()#ilk 5 kayit 
result = data.head(10)#ilk 10 kayit
result = data.tail()# son 5 kayit
result = data["Movie_Title"]#sadece filmin ismi 
result = data["Movie_Title"].head()
result = data[["Movie_Title","Rating"]].head()
result = data[["Movie_Title","Rating"]].tail(7)
result = data[5:][["Movie_Title","Rating"]].head()# ikinci 5 kayit 
result = data[data["Rating"]>=8.0][["Movie_Title","Rating"]].head(50)
result = data[(data["YR_Released"]>=2014) & (data["YR_Released"]<=2015 )][["Movie_Title","YR_Released"]]
data_ = data["YR_Released"]
simdi = 2023
data['Age_Movie'] = [simdi - YR_Released for YR_Released in data_]
# print(result)
data.to_csv('imdb.csv', index=False)
result = data[data["Movie_Title"].str.startswith("A")]


print(result)