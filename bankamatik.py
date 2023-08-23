AnasHesap = {
    'ad':'Anas Eskander',
    'hesapNo':'12345678',
    'bakiye':3000,
    'ekHesap':2000
}
AhmetHesap = {
    'ad':'Ahmet',
    'hesapNo':'12345678',
    'bakiye':2000,
    'ekHesap':1000
}
def para_cek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if(hesap['bakiye']>=miktar):
        hesap['bakiye'] -= miktar
        print('Paranizi alabilirsiniz..')
        print(f"İşlem yaptıktan sonra {hesap['hesapNo']} nolu hesapinizda {hesap['bakiye']} TL ve ek hesapinizda {hesap['ekHesap']} bulunmaktadir") 

    else:
        toplam = hesap['bakiye']+hesap['ekHesap']
        if(toplam>=miktar):
            ekhesapkullanma = input('Bakiyeniz yetersiz ek hesapiniz kullanmak istiyor musunuz (e\h) ? ')
            if ekhesapkullanma=='e':
                ekhesapkullanilacakmiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap']-=ekhesapkullanilacakmiktar
                print('Paraninzi alabilirsiniz')
                print(f"İşlem yaptıktan sonra {hesap['hesapNo']} nolu hesapinizda {hesap['bakiye']} TL ve ek hesapinizda {hesap['ekHesap']} bulunmaktadir") 

            else:
             print(f"{hesap['hesapNo']} nolu hesapinizda {hesap['bakiye']} bulunmaktadir") 
        else:
            print("Uzgunuz bakiye yetersiz")


para_cek(AnasHesap,3000)
para_cek(AnasHesap,1000)
