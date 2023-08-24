# Fonksiyon: Verilen öğrenci notlarını hesaplar ve harf notunu döndürür
def not_hesapla(satir):
    # Satır sonundaki boşluğu kaldırarak öğrenci adını al
    satir = satir[:-1]
    dizi = satir.split(':')  # Satırı ':' karakterine göre böler ve iki elemanlı bir dizi oluşturur
    ogrenci_adi = dizi[0]
    notlar = dizi[1].split(',')  # Notları ',' karakterine göre böler ve notlar listesi oluşturur

    # Notları integer'a çevir
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    # Ortalamayı hesapla
    ortalama = (not1 + not2 + not3) / 3

    # Ortalamaya göre harf notunu belirle
    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 75 and ortalama <= 84:
        harf = "BB"
    elif ortalama >= 65 and ortalama <= 74:
        harf = "CB"
    elif ortalama >= 55 and ortalama <= 64:
        harf = "CC"
    elif ortalama >= 50 and ortalama <= 54:
        harf = "DC"
    elif ortalama == 50:
        harf = "DD"
    else:
        harf = "FF"

    return ogrenci_adi + ": " + harf + "\n"

# Dosyadan öğrenci notlarını okuyup hesaplar ve ekrana yazar
def ortalamalari_oku():
    try:
        with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
            for satir in file:
                print(not_hesapla(satir))
    except FileNotFoundError as ex:
        print("Dosya ismi hatalıdır", ex)

# Öğrenci adı, soyadı ve notları alarak dosyaya kaydeder
def not_gir():
    ad = input("Ogrenci adi: ").strip()
    soyad = input("Ogrenci soyadi: ")
    not1 = input("Not 1: ")
    not2 = input("Not 2: ")
    not3 = input("Not 3: ")

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3 + '\n')

# Öğrenci notlarını okuyup hesaplar, harf notlarını dosyaya kaydeder
def notlari_kayitet():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    # Kullanıcıya yapılacak işlemi sor
    islem = input("1- Notlari oku\n2- Not gir\n3- Notlari kayit et\n4- Cikis\n")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayitet()
    else:
        break  # Kullanıcı çıkış seçeneğini seçerse döngüyü sonlandır
