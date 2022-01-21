#7 – Kérjünk be egy számot és egy másikat úgy, hogy nagyobb legyen az elsőnél. Számoljunk visszafelé a nagyobbik számtól a kisebbik felé. (A feladat kiegészíthető azzal, hogy bekérjük a lépésközt is, ami kisebb kell legyen a két szám különbségénél.)

kezdoErtek:int = None
data1:str =""
vegErtek: int = None
data2:str= ""

while(kezdoErtek == None):
    data1 = input("Adja meg a kezdőértéket:")
    if(data1.replace("-", "").isnumeric()):
        kezdoErtek = int(data1)
    else:
        print("Nem számot adott meg")

while(vegErtek == None or vegErtek <= kezdoErtek):
    data2 = input("Adja meg a végértéket:")
    if(data2.replace("-", "").isnumeric()):
        vegErtek = int(data2)     
    else:
        print("Nem számot adott meg")

for i in range(kezdoErtek, vegErtek+1, 1):
    print(i, end=" " )
print()