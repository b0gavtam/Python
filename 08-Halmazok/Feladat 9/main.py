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

halmaz: List[int] = []
elemekSzama:int = None



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
    for i in range(elem + 1):
        eredmeny.append(random.randint(-100,100))
        time.sleep(0.005)

    return eredmeny

def halmazKiirasa(kiirandoHalmaz:List[int])-> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")



def szetvalasztas()-> Dict[str, List[int]]:
    dictionary: Dict[str, List[int]] = { "pozitivHalmaz" : [], "negativHalmaz" : [] }





elemekSzama= elemszamBekerese()
halmaz = ListaFeltoltesekRandomSzamokkal(elemekSzama)
print("A halamaz elemei: \t")
halmazKiirasa(halmaz)    