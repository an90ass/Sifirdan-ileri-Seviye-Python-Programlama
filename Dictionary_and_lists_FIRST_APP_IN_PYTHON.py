sayi_1 = input('sayi_1: ')
sayi_2 = input('sayi_2: ')
sayi_3 = input('sayi_3: ')

print(type(sayi_1))
toplam = int(sayi_1) + int(sayi_2) + int(sayi_3)
print(type(sayi_1))

print("Toplam:", toplam)

r = float(input('r: '))
bay = 3.14
alan = (int(r) ** 2) * bay
cevre = r * bay * 2
print("Alan =", str(alan) + " Cevre =", str(cevre))

r = 'Hello There . My name is Anas'.split()
a = ' Hi'.split()
b = r + a

ad = 'anas'
soyad = 'almaqtari'
result = f'Benim adım {ad} soyadım {soyad}'
print(result)

users = {
    'anas': {
        'age': 30,
        'email': 'ana@gmail.com',
        'phone': 71414141,
        'rolse': ['User', 'Admin']
    },
    'ahmed': {
        'age': 14,
        'email': 'ha@gmail.com'
    }
}

print(users['anas']['rolse'][0])

ogrenciler = {}
number = input("Student number: ")
name = input("Student name: ")
surename = input("Student surename: ")
phone = input("Student phone: ")

ogrenciler[number] = {
    'name': name,
    'surename': surename,
    'phone': phone
}

number = input("Student number: ")
name = input("Student name: ")
surename = input("Student surename: ")
phone = input("Student phone: ")

ogrenciler.update({
    number: {
        'name': name,
        'surename': surename,
        'phone': phone
    }
})

print(ogrenciler)
print('*' * 50)

ogrno = input("Öğrenci numara giriniz: ")
print(ogrenciler[ogrno])

vize1 = float(input('vize1: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
result = (ortalama > 50)
print(f'Ortalama = {ortalama} ve geçme notu = {result}')

if 2 < 3:
    print('Merhaba')
