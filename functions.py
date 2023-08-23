name = 'anas'

def hellow(name='Ahmet'):
    return 'Hello ' + name

a = hellow(name)
print(a)

def num(a, b):
    return a + b

result = num(10, 20)
print(result)

def yashesapla(dogum_yili):
    return 2023 - dogum_yili

def emiklilige_kac_kaldi(dogumtarihi, isim):
    yas = yashesapla(dogumtarihi)
    emiklilik = 65 - yas
    if emiklilik > 0:
        print(f'{isim} emekliliğinize {emiklilik} yıl kaldı. Yaşınız şu an {yas} yıl.')
    else:
        return f'{isim} zaten emekli oldunuz. Yaşınız {yas} yıl.'

anas = emiklilige_kac_kaldi(2002, 'anas')
ahmet = emiklilige_kac_kaldi(2000, 'ahmet')

def listeyecevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

result = listeyecevir(10, 20, 30, 'merhaba')
print(result)

def asalhesaplama(sayi1, sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input('Sayı 1 giriniz: '))
sayi2 = int(input('Sayı 2 giriniz: '))
asalhesaplama(sayi1, sayi2)

def square(number):
    return number ** 2

liste = [1, 2, 3, 4, 5, 6]
for item in map(square, liste):
    print(item)

result = list(map(square, liste))
print(result)

liste = [1, 2, 3, 4, 5, 6]
square = list(map(lambda num: num ** 2, liste))
result = list(map(lambda num: num ** 2, liste))
for item in square:
    print(square)

def check_even(num):
    return num % 2 == 0

result = list(filter(check_even, liste))
print(result)
