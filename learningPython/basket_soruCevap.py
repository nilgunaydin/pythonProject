sorular =[]
cevaplar = []
cevap = ""
soru =""
print
while soru != "Tamam":
    soru = input  ("Ülke giriniz   :")
    if soru == "Tamam" : break
    cevap = input ("Başkent giriniz:")

    sorular.append(soru)
    cevaplar.append(cevap)

print (len(sorular), "adet soru girdiniz.")
print ("Girdiğiniz sorular:", sorular)
print ("Girdiğiniz cevaplar:", cevaplar)
sorular.sort()
cevaplar.sort()
print ("Girdiğiniz sorular(sıralanmış) :", sorular)
print ("Girdiğiniz cevaplar(sıralanmış):", cevaplar)
print(sorular[0])


