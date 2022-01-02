i=5
while i<=10:
    i += 1
    print(i)

a = 20
while a <= 30:
    a +=1
    if a%5 ==0 : continue
    print(a)
else:
    print ("a değeri 30'dan küçük değil")

    print("Ders notlarınızın ortalamasını hesapla.")
    print("Not girişi bittiğinde boşluk giriniz.")
    ortalama = 0
    toplam = 0
    notsayisi = 0
    dersnotu = ""

while dersnotu != " ":
        dersnotu = input("Ortalaması alınacak notu giriniz:")
        if dersnotu == " ": break
        toplam += int(dersnotu)
        notsayisi += 1
ortalama = toplam / notsayisi
print("Ortalamanız:", ortalama)
