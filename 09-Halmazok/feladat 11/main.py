"""11. Töltsünk fel egy listát a felhasználó által megadott elemszámmal (min 10). A lista elemei legyenek véletlen számok -100 és 100 közt. Hozzunk létre két új halmazt, ahol:
- az A halmaz elemei azok a halmaz elemek melyek oszthatóak 3-al
- a B halmaz elemei azok a halmaz elemek melyek oszthatóak 5-el, de nem oszthatóak 3-al
Mely halmaz (A vagy B) átlaga a nagyobb?
A képernyőre írassuk ki az eredeti listát, az A, illetve B halmazt is."""
from typing import *
import random

halmaz:List[int] = []
aHalmaz:List[int] = []
bHalmaz:List[int] = []
elemekSzama:int = None
osszeg:int = None




def elemszambekerese()-> int:
    eredmeny:int = None
    while(eredmeny == None or eredmeny < 10):
        data:str = input("Kérem adja meg a halmaz méretét (minimum 10 szám): ")
        if(data.isdigit()):
            eredmeny = int(data)
        else:
            print("Nem számot adott meg!")

    return eredmeny



def listafeltolteserandomszamokkal(elemekSzama: int)-> List[int]:
    eredmeny: List[int] = []
    for i in range(elemekSzama):
        eredmeny.append(random.randint(-100, 100))

    return eredmeny

def  ahalmazfeltoltese(elemekSzama)-> List[int]:
    eredmeny:List[int] = []
    for i in range(elemekSzama):
        if(i % 3 == 0):
            eredmeny.append(aHalmaz[i])  

    return eredmeny

def  bhalmazfeltoltese(elemekSzama)-> List[int]:
    eredmeny:List[int] = []
    for i in range(elemekSzama):
        if(i % 5 == 0 and i % 3 != 0):
            eredmeny.append(bHalmaz[i]) 
    
    return eredmeny

def osszegszamolas(kereseshalmaz:List[int])-> int:
    eredmeny:int = None
    for item in kereseshalmaz:
        eredmeny += item

    return eredmeny


elemekSzama = elemszambekerese()
halmaz = listafeltolteserandomszamokkal(elemekSzama)
print(halmaz)

aHalmaz = listafeltolteserandomszamokkal(elemekSzama)
bHalmaz = listafeltolteserandomszamokkal(elemekSzama)
print(aHalmaz)
print(bHalmaz)
