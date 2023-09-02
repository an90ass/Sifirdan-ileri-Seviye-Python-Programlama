from datetime import datetime
simdi = datetime.now()#2023-08-26 18:26:01.695552
# simdi = datetime.today()#2023-08-26 18:26:01.695552
year = simdi.year #2023
month = simdi.month #8
day = simdi.day #26
hour = simdi.hour #18
minute = simdi.minute # 31
ctime = datetime.ctime(simdi) #Sat Aug 26 18:36:18 2023


strftime = datetime.strftime(simdi,'%Y')#2023
strftime = datetime.strftime(simdi,'%X')#18:43:39
strftime = datetime.strftime(simdi,'%d')#26
strftime = datetime.strftime(simdi,'%A')# Saturday
strftime = datetime.strftime(simdi,'%B')#August

t = '28 August 2023 hour 18:48:30'
dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S' )#2023-08-28 18:48:30

birthday = datetime(2002,7,3,12,30,12)#2002-07-03 12:30:12
result = datetime.timestamp(birthday) # saniye 1025688612.0
result = datetime.fromtimestamp(result) # saniye to datetime

result = datetime.fromtimestamp(0) # saniye to datetime

result = simdi - birthday # 7724 days, 6:30:20.064366
print(result)




