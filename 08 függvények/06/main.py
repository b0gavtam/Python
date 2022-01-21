import random
import os
import time

elsoSzam:int=None
masodikSzam:int=None
titkos:int=None

def szamBekeres(kezdoErtek:int, vegErtek:int, text:str)->int:
    eredmeny:int=None
    while (eredmeny==None):
        data:str=input(text)
        if (data.replace("-","").isdigit()):
            if (int(data) >= kezdoErtek and int(data) <= vegErtek):
                eredmeny=int(data)
                return eredmeny
            else:
                print("Nem a 2 érték között adott számot!")
        else:
            print("Nem számot adott meg!")
    
def tippBekeres()->int:
    eredmeny:int=None
    while (eredmeny==None):
        data:str=input("Kérem a tippet: ")
        if (data.isdigit()):
            eredmeny=int(data)
            return eredmeny
        else:
            print("Nem számot adott meg!")

def tipp(tipp:int, szam:int, probakSzama:int)->None:
    if(tipp > szam):
        print("A kitalálandó szám kisebb")
    elif(tipp < szam):
        print("A kitalálandó szám nagyobb")
    else:
        print(f"Próbálkozások száma: {probakSzama}\nA kitalálandó szám: {szam}")

def jatek(szam:int)->None:
    probalkozasokSzama:int=0
    ertek:int=0

    while(ertek != szam):
        ertek = tippBekeres()
        probalkozasokSzama+=1
        tipp(ertek, szam, probalkozasokSzama)

elsoSzam=szamBekeres(0, 9, "Kérek egy számot 0 és 9 között: ")
masodikSzam=szamBekeres(40, 50, "Kérek egy számot 40 és 50 között: ")
titkos=random.randint(elsoSzam, masodikSzam)

jatek(titkos)