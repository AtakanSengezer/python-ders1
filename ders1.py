# degiskenBir = "Atakan"
# degisken_İki = "Sengezer"
# print(degiskenBir)

# 1sayi = #değişkenler sayi ile başlamaz

""" a,b,c = 10,15,20
print(a,b,c)  <<< çoklu yorum satırı alt + shit + a  """ 

# ! Değer tanımlama
# urun_a = 7000
# kdv = 0.18
# print(urun_a + (urun_a * kdv))  

#  TODO : Uygulama
""" Aşağıdaki ürünler için değişken oluşturup toplam bilgisini hesaplayın
urun 1 > 50 tl
urun 2 > 60tl 
urun 3 152.40 tl
  """


# urun1 = 50
# urun2 = 60
# urun3 = 152.40
# toplam = (urun1 + urun2 + urun3)
# print(toplam)

# ! Veri Tipleri
# İNT FLOAT
# STRİNG
# LİST
# TUPLE
# DİCTİONARY
# BOOL

# ! Sayı Veri Tipleri Int float
# * py bir sayı tanımlaması yaparken kullanabileceğimaiz 2 veri tipi vardır intger ve float veri tipleri intger tam sayı , float ise ondalıklı sayıdır. rakamdan sonra nokta varsa float olarak algılanır yoksa int olarak algılanır;

# print(2+2)
# print(type(2))
# print(type(2.5))
# print(type("2 +2 "))

# ! Sayısal Operatörler
#* temel operatörler
#  print(3+4) #Toplama
#  print(type(3+4))

# print(25-11) #Çıkarma
# print(10/5) #Bölme 
# print(2*4) #çarpma

 #* Gelişmiş Operatörler
# print(2**3) #Üsalma
# print(10%2) #Mod Alma
# print(10//3) #tambölme

# !String 
# * Herhangi bir karakter dizesine string denir. Tek bir harften oluşacağı gibi bir çok harften ve rakamdan da oluşabilir 

# ad = "Abdulkadir"
# soyad = "kizilarslan"
# cinsiyet = "e"
# sehir = "izmir"
# yas = "26"

# print(ad,soyad)
# # print(type(ad,soyad))  << iki veri yazdıramayız
# print(type(ad+soyad))
# print(ad[2])
# print(ad[-2])

# ! string slicing
# print(ad[0:3])  # 0-3 arasını yazdırır 3.index dahil değildir
# print(ad[:3]) #yukardaakının aynısı
# print(ad[5::]) # 5.index ten bitişe kadar
# print(ad[::2]) # 0 dan başlar 2 atlayarak gider
# print(ad[::-1])  #tersten yazar

ad = "abdulkadir"
soyad = "kizilarslan"
cinsiyet = "e"
sehir = "izmir"
yas = "26"

#! String Metodları
#* Upper metodu karakterleri büyük harfe çevirir
# print(ad.upper())

# # *Lower metodu karakterleri küçük harfe çevirir
# print(ad.lower())

# *Title kelimenin ilk harfini büyük harfe çevirir
# print(ad.title())

# * Replace metodu karakter güncellemesi için kullanılır
# print(ad.replace("abdulkadir" , "atakan"))

# * Strip metodu metodu ile karakter dizisinin başındaki ve sonundaki boşlukları silebiliriz 
# name = "     kadir     "
# print(name)
# print(name.strip())

# * index ile aradığımız karakterin kaçıncı satırda oluğunu yazar
# print(ad.index("a")) 

# *is meetodları
# * is_lower küçük harf içeriyor mu ?
# print(ad.islower())

# ! String Formatlama
# print("benim adım" + ad + " soyadım " + soyad + " ve ben " + sehir + " de yaşıyorum.")
# print("Benim Adım", ad,"soyadım",soyad,"ve ben", sehir ,"de yaşıyorum")
# print("Benim adım {} soyadım {} ve ben {} de yaşıyorum".format(ad,soyad,sehir))
# print(f"Benim adım {ad} soyadım {soyad} ve ben {sehir} de yaşıyorum")

# print("Benim Adım", ad, "\n soyadım",soyad,"ve ben \n", sehir ,"de yaşıyorum")

website = "https://www.neosyazilim.com/"
kursAdi = "Python Dersleri : Sıfırdan ileri seviye Python Programlama"

# *1 = kursAdi karakter dizesinde kaç karakter vardır ?
# print(len(kursAdi))

# *2 "website" içinde www karakterlerini yazın ?
# print(website.index("w"))
# print(website[8:11])

# * "website" içindeki com karakterini yazın ?
# print(website[-4: -1])

# * 4 KursAdi içerisindeki ilk 15 ve son 15 karakteri yazın ?
# print(kursAdi[0:15])
# print(kursAdi[-15:])
# print(kursAdi[::-1]) # tersten yazdık

# * "Hello world" ifadesindeki w harfini "W" ile değiştirin 
helloWorld = "       Hello world "
# print(helloWorld.replace("w" , "W"))
# helloWorld = "HELLO" 
# print(helloWorld)

# * "abc" ifadesini yan yana 3 defa yazdırın?
# print(" abc" *3)

# *7 "Hello World" içindeki boşlukları silin
# print(helloWorld.strip()) # <<< Komple siler
# print(helloWorld.lstrip()) # <<< sol taraftan siler
# print(helloWorld.rstrip())  # <<< sağ taraftan siler


# *8 "kursadi" tüm karakterleri küçük harf yapın

# print(kursAdi.lower())

# *9 "website" içinde kaç tane "w" karakteri var ?
# print(website.count("w"))

# *10 "website" www ile mi başlıyor ?
# print(website.startswith("www"))
# print(website.endswith("com/"))


# ! Listeler
# * Liste , elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir. Ve farklı veri tiplerindeki bilgieri barındırabilir.

# mesaj = "merhaba dünya , ben kadir".split()

# print(mesaj)
# print(mesaj[0])

isimler = ["Kadir", 26 ,"Ahmet" , 30 , "Mert" , 25 , "Muhammed" , 24 ,"Yusuf" , 31 , "Atakan" , 21  ]
isimler_iki =[["Kadir", 26],["Ahmet" , 30],[ "Mert" , 25],["Muhammed" , 24],["Yusuf" , 31 ],["Atakan" , 21]]
# print(isimler)
# print(type(isimler))
# print(isimler_iki)
# print(isimler_iki[5][0]) # << liste içinden seçtiğimiz indeksin içinden indeks seçmek

# print(isimler + isimler_iki)

# ! Liste slicing

# isimler[0] = "Abdulkadir"
# print(isimler[::2])

# print(isimler + ["Emre",30])

# del isimler[0]
# print(isimler)