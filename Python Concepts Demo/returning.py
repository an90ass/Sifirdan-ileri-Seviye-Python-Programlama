
def usalma(number):
    def inner(power):
        return number ** power
    return inner

two = usalma(2)
three = usalma(3)
print(two(3))  # Bu 2^3'ü hesaplayacak ve 8'i yazdıracaktır
print(three(4))# Bu 3^4'ü hesaplayacak ve 81'i yazdıracaktır

print("*************************************** yetki sorgula ornek *************************************** ")
'''
yetki sorgula ornek 
'''
def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return "{0} rolu {1} sayfasina olasabilir.".format(role,page)
        else:
             return "{0} rolu {1} sayfasina olasamaz.".format(role,page)
    return inner
user = yetki_sorgula("Product edit")
print(user("Admin"))
print(user("User"))

print("***************************************  islem ornek *************************************** ")

def islem(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam
        
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *=i
        return carpim
    def azaltma(*args):
        azaltma = 0
        for i in args:
            azaltma -=i
        return azaltma
    
    if islem_adi =="toplama":
        return toplama
    elif islem_adi =="carpma":
        return carpma
    elif islem_adi =="azaltma":
        return azaltma
    else:
        raise ValueError("Geçersiz işlem adı")

try:
    carpma = islem("carpma")
    print(carpma(1, 2, 3, 4, 5))
    
    # Geçersiz bir işlem adı ile deneme
    test_islem = islem("bölme")
except ValueError as e:
    print("Hata:", e)