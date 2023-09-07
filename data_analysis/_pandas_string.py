import pandas as pn

data = pn.read_csv("datasets/ba.csv")
data.dropna(inplace=True)
# df = pn.DataFrame(data)
# data["Name"]= data["Name"].str.upper()
# data["Name"]= data["Name"].str.lower()
# data["index_a"] = data["Name"].str.find("a")
data = data[data["Name"].str.contains("Jordan")]
data = data[data.Name.str.contains("Jordan")]
data[['FirstName','LastName']]= data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)

print(data.head(10))