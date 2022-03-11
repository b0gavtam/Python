from typing import *
import random
import time




aHalmaz:List[int]= []
bHalmaz:List[int] = []
abHalmaz:List[int] = []
elemekSzama: int = None



def elemszambekerese()-> int:
    eredmeny: int = None
    while(eredmeny == None or eredmeny < 2):
        temp:str = input("Kérem adja meg a halmazok adatainak számát: ")
        if(temp.isdigit()):
            eredmeny = int(temp)
        else:
            print("Nem számot adott meg!")

    return eredmeny   

def listaFeltolteseRandomSzamokkal(elemekSzama: int)-> List[int]:
    eredmeny: List[int] = []
    for i in range(elemekSzama):
        eredmeny.append(random.randint(-100,100))

    return eredmeny

def unio(aHalmaz:List[int], bHalmaz:List[int], elemekszama:int)-> List[int]:
    eredmeny:List[int] = [] 
    for i in range(elemekszama):
        eredmeny.append(aHalmaz[i])
        eredmeny.append(bHalmaz[i])
        
        
    return eredmeny



elemekSzama = elemszambekerese()
aHalmaz = listaFeltolteseRandomSzamokkal(elemekSzama)
bHalmaz = listaFeltolteseRandomSzamokkal(elemekSzama)
abHalmaz = unio(aHalmaz,bHalmaz, elemekSzama)

print(f"A halmaz: {aHalmaz}")
print(f"B halmaz: {bHalmaz}")

print(f"A két halmaz egyben: {abHalmaz}")