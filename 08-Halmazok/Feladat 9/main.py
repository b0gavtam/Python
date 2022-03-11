"""lépések:
1. elem számok beolvasása-> int
2. elemek szétválasztása-> List[int]
def szetvalasztas(hataretek:int, lista:List[int])->List[int]
    if(szam >=-1):
    if(szam <= -1):    

negatív
szetvalasztas(-1, halmaz)

pozitív
szetvalasztas(1, halmaz)
"""

from typing import *
import random
import time


halmaz: List[int] = []
elemekSzama:int = None
eredmenySzotar:Dict[str, List[int]] = {}


def elemszamBekerese()-> int:
    eredmeny:int = None
    temp: str = None

    while(eredmeny == None):
        temp:str = input("Kérem adja meg a halmaz elemeinek számát: ")
        if(temp.isdigit()):
            eredmeny = int(temp)
        else:
            hiba("Nem számot adott meg!")

    return eredmeny

def ListaFeltoltesekRandomSzamokkal(elem:int)-> List[int]:
    eredmeny: List[int] = []
    for i in range(elem):
        eredmeny.append(random.randint(-100,100))
        time.sleep(0.005)

    return eredmeny

def halmazKiirasa(kiirandoHalmaz:List[int])-> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")



def szetvalasztas(lista:List[int])-> Dict[str, List[int]]:
    dictionary: Dict[str, List[int]] = { "pozitivHalmaz" : [], "negativHalmaz" : [] }
     
    for item in lista:
        if(item > 0):
            dictionary["pozitivHalmaz"].append(item)
        elif(item < 0):
            dictionary["negativHalmaz"].append(item)    

    return dictionary        




elemekSzama= elemszamBekerese()
halmaz = ListaFeltoltesekRandomSzamokkal(elemekSzama)
print("A halamaz elemei: \t")
halmazKiirasa(halmaz)
eredmenySzotar = szetvalasztas(halmaz)

print("Pozitív számok halmaza: ")
print(eredmenySzotar["pozitivHalmaz"])


print("Negatív számok halmaza: ")
print(eredmenySzotar["negativHalmaz"])