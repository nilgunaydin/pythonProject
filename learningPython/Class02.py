import random
konu= "Cekilis Programi"
print(konu)
print("-"*len(konu),"\n")

print("Cekilisi yapilacak ogrencilerin isimleri giriniz:")

ogrenciler = []
ogrenci=""


while ogrenci!="Bitti" :
    ogrenci=input("isim girdikten sonra enter a basiniz:")
    if ogrenci!="Bitti" :
        ogrenciler.append(ogrenci)

print("cekiliste",len(ogrenciler),"adet ogrenci var")
print("kazanan ogrenci:",ogrenciler[random.randint(0,len(ogrenciler)-1)])
