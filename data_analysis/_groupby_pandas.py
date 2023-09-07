import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}


data = pd.DataFrame(personeller)
result = data
result = data.groupby("Departman").groups
result= data.groupby(["Departman","Semt"])
result = data.groupby("Semt")
# for name,value in result:
#     print(name)
#     print(value)
result = data.groupby("Semt").get_group("Tuzla")
result = data.groupby("Departman").get_group("Muhasebe")
result = data.groupby("Departman").sum()
result = data.groupby("Departman").max()
result = data.groupby("Departman")["Maaş"].mean()
result = data.groupby("Semt")["Yaş"].mean()
result = data.groupby("Semt")["Yaş"].min()
result = data.groupby("Semt")["Çalışan"].count()
result = data.groupby("Departman")["Maaş"].min()["Muhasebe"]
result = data.groupby("Çalışan")["Maaş"].min()
# result = data.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]





print(result)
