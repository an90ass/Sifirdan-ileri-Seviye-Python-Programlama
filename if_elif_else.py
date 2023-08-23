
for a in range(1, 11):
    print(a)

name = ''
while not name:
    name = input('name: ')
print(f'merhaba, {name}')

sayiler = [1, 3, 5, 7, 9, 12, 19, 21]
i = 0
while i < len(sayiler):
    print(sayiler[i])
    i = i + 1

numbers = []
i = 0
while i < 5:
    number = int(input('sayiler: '))
    numbers.append(number)
    i = i + 1

for b in numbers:
    if b % 2 == 0:
        print(b)

urunler = []
adet = int(input('Kaç tane ürün eklemek istiyorsunuz? '))
i = 0
while i < adet:
    urun = input("Ürün ismi giriniz: ")
    fiyat = input("Fiyat ismi giriniz: ")
    urunler.append({
        'isim': urun,
        'fiyat': fiyat
    })
    i += 1

for urun in urunler:
    print(f"Ürün adı: {urun['isim']} Ürün fiyatı {urun['fiyat']}")    

numbers = [x for x in range(10)]
print(numbers)

import random

sayi = random.randint(1,50)
can = int(input("Sayi bulmak icin kac hak kullanmak istiyorsunuz ? "))

hak = can
sayac =0
while hak >0:
    hak = hak-1
    sayac +=1
    tahmin = int(input("Tahmin ? "))
    if(tahmin == sayi):
        print(f'Tebrikler {sayac}.defada bildiniz sayi = {sayi} .. Toplam puaniniz = {100-(20)*(sayac-1)}')
        break
    elif(tahmin<sayi):
        
        print("yukari") 
    else:
        print("asagi") 
    if hak==0:
        print(f'hakkiniz bitti sayi = {sayi}') 