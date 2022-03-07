"""4. Töltsünk fel egy listát [-100, 100 közt] a felhasználó által megadott elem számmal. E listából távolítsuk el a negatív előjelű elemeket. Ezen elemekből (eltávolítottak) készítsünk egy új listát."""



from typing import *
import random

halmaz: List[int] = []
elemekSzama:int = random.randint(10,20)
pozitivhalmaz: List[int] = []

def listaFeltolteseRandomSzamokkal(elem:int)-> List[int]:
    eredmeny: List[int] = []
    for i in range(elem + 1):
        eredmeny.append(random.randint(-100,100))

    return eredmeny

def halmazKiirasa(kiirandohalmaz:List[int])-> None:
    for item in kiirandohalmaz:
        print(f"{item}", end="  ")

def pozitivhalmazFeltoltese(halmaz:List[int])-> List[int]:
    eredmeny: List[int] = []
    for item in halmaz:
        if(item >= 0):
            eredmeny.append(item)
        
    return eredmeny
    








#főprogram
halmaz = listaFeltolteseRandomSzamokkal(elemekSzama)
print("Az eredeti halmaz: ")
halmazKiirasa(halmaz)

pozitivhalmaz = pozitivhalmazFeltoltese(halmaz)
print("\nA pozitív számok halmaza: ")
halmazKiirasa(pozitivhalmaz)