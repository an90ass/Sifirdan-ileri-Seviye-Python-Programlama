import pandas as pn

df = pn.read_csv("datasets/nba.csv")

result = df.head(5)#ilk 5 kayit
result = len(df.index)#toplam kac kayit vardir
result = df["Salary"].mean()#tum oyuncularin toplam maas ortalamasi
result = df["Salary"].max()#en yuksek maas
result = df[df["Salary"]==df["Salary"].max()]# en yuksek maas alan kisinin bilgileri
result = df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]# en yuksek maas alan kisinin ismi
result = df[(df["Age"]>=20 )& (df["Age"]<25)][["Name","Team","Age"]].sort_values("Age",ascending=False)#Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan sirali şekilde 
result = df[df["Name"] == "John Holland"]["Team"].iloc[0] #"John Holland" isimli oyuncunun oynadığı takım hangisidir ?
# result = df.groupby("Team").mean()["Salary"]       #Takımlara göre oyuncuların ortalama maaş bilgisi (bu satir hata verir)
result = len(df.groupby("Team"))# Kaç farklı takım mevcut ?
result = df["Team"].nunique()# Kaç farklı takım mevcut ?
result = df["Team"].value_counts()#Her takımda kaç oyuncu oynamaktadır ?
# İsmi içinde "and" geçen kayıtları bulalim.
df.dropna(inplace = True)
result = df[df["Name"].str.contains("and")]
def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)]
# print(df)
print(result)

