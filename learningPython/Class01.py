def abc():
    global t
    t = "merhaba"


abc()
a=10
b=10.5
c="ankara"
print(c)
print(type(c))
print(type(b))
print(t)

#degisken ve sabit ornegi

konu = "DAİRENİN ALAN VE ÇEVRE HESABI"
print (konu)
print ("-"*len(konu))
r = int (input("Dairenin yarıçapı nedir?"))
# yaricap değişen bir ifadedir
pi = 3.14
# çift tırnak içindeki metinler sabit ifadedir
print ("Dairenin çevresi = ",2 * pi * r)
print ("Dairenin alanı   = ",pi * r * r)

