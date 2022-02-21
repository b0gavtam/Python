"""2. Töltsünk fel egy listát véletlenszerű 3 jegyű egész számokkal
	Számítsuk ki az elemek összegét
	Számítsuk ki az elemek átlagát
	Számoljuk meg hány szám van 500 felett!"""


from typing import *
import random
import os
import time

halmaz: List[int] = []
elemekSzama:int = random.randint(10,20)
osszeg:int = None
szam:int = None
otszazontul: int = None

def hiba(uzenet:str)-> None:
    print(uzenet)
    time.sleep(2)
    os.system("cls")


def ListaFeltolteseRandomSzamokkal(elem:int)-> List[int]:
    eredmeny: List[int] = []
    szorzo:int = 1
    for i in range(0, elem, 1):
        szam = random.randint(100, 999)
        eredmeny.append(szam * szorzo)
        szorzo*=-1

    return eredmeny

def halmazKiirasa(kiirandoHalmaz:List[int])-> None:
    for szam in kiirandoHalmaz:
        print(f"{szam}", end="\t")


def szamokOsszege(keresesHalmaza:List[int])-> int:
    eredmeny:int = 0
    for item in keresesHalmaza:
        eredmeny += item

    return eredmeny

def otszazonfeluliszamokszama(kiirandoHalmaz:List[int])-> int:
    eredmeny: int = 0
    for item in kiirandoHalmaz:
        if (item > 500):
            eredmeny +=1
    
    return eredmeny


#főprogram
halmaz = ListaFeltolteseRandomSzamokkal(elemekSzama)
halmazKiirasa(halmaz)

osszeg = szamokOsszege(halmaz)
print(f"\nA számok összege: {osszeg}")
print(f"\nA számok átlaga: {osszeg / elemekSzama}")

otszazontul = otszazonfeluliszamokszama(halmaz)
print(f"\nAz ötszáznál nagyobb számok száma: {otszazontul}")