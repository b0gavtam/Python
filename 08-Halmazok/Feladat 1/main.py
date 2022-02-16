"""Töltsünk fel egy listát a felhasználó által megadott elemű random számokkal:"""
from typing import *
import random
import os
import time

halmaz: List[int] = []
elemekSzama:int = None
osszeg:int = None
ketjegyuszamok = None
paratlanszamokosszege = None

def hiba(uzenet:str)-> None:
    print(uzenet)
    time.sleep(2)
    os.system("cls")

def elemszamBekerese()-> int:
    eredmeny:int = None
    temp: str = None

    while(eredmeny == None):
        temp:str = input("Kérem adja meg a halmaz elemeinek számát: ")
        if(temp.isdigit()):
            eredmeny = int(temp)
            if(eredmeny < 2):
                hiba("A halmaz elemeinek számának legalább kettőnek kell lennie!")
        else:
            hiba("Nem számot adott meg!")

    return eredmeny

def ListaFeltoltesekRandomSzamokkal(elem:int)-> List[int]:
    eredmeny: List[int] = []
    for i in range(elem + 1):
        eredmeny.append(random.randint(-10,10))
        time.sleep(0.005)

    return eredmeny


def halmazKiirasaForditottSorrendben(kiirandoHalmaz:List[int])-> None:
    max:int = len(kiirandoHalmaz) - 1
    for index in range(max, -1, -1):
        print(f"{kiirandoHalmaz[index]}", end="\t")


def halmazKiirasa(kiirandoHalmaz:List[int])-> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")

def ketjegyuszamokszama(keresesHalmaza:List[int])-> int:
    eredmeny: int = 0
    for item in keresesHalmaza:
        if(abs(item) > 9 and abs(item) < 100):
            eredmeny +=1
    
    return eredmeny

def egyjegyuszamokszama(keresesHalmaza:List[int])-> int:
    for item in keresesHalmaza:
        if(abs(item) < 10):
            print(f"{item}", end="\t")
    
def paratlanSzamokOsszege(keresesHalmaza:List[int])-> int:
    eredmeny:int = 0
    for item in keresesHalmaza:
        if(item % 2 == 1):
            eredmeny += item

    return eredmeny

def parosSzamokKiirasa(kiirandoHalmaz:List[int])-> None:
    for item in kiirandoHalmaz:
        if(item % 2 == 0):
            print(f"{item}", end="\t")

def sum(osszeadandoHalmaz:List[int])-> int:
    eredmeny:int = 0
    for item in osszeadandoHalmaz:
        eredmeny += item
    
    return eredmeny

#főprogram

elemekSzama= elemszamBekerese()
halmaz = ListaFeltoltesekRandomSzamokkal(elemekSzama)
os.system("cls")

print("A halamaz elemei: \t")
halmazKiirasa(halmaz)


#Írassuk ki fordított sorrendben
print("\nA halmaz elemeinek kiírása fordított sorrendben: \t")
halmazKiirasaForditottSorrendben(halmaz)

#Számítsuk ki az elemek összegét
osszeg = sum(halmaz)
print(f"\nA halmaz elemeinek összege:{osszeg}")

#Átlagoljuk a tömbelemeket
print(f"\nA halmaz elemeinek átlaga: {osszeg / elemekSzama}")

#Írassuk ki a páros elemeket
print(f"\nA halmaz páros elemei:")
parosSzamokKiirasa(halmaz)

#Számoljuk meg hány kétjegyű szám van a tömbben
ketjegyuszamok = ketjegyuszamokszama(halmaz)
print(f"\nA halmazban {ketjegyuszamok} kétjegyű szám van.")

#Írassuk ki az egyjegyű számokat
print("\nA halmaz egyjegyű elemei:")
egyjegyuszamokszama(halmaz)

#Számítsuk ki a páratlan számok összegét
print(f"\n A halmaz páratlan elemeinek összege: {paratlanszamokosszege}")
paratlanszamokosszege = paratlanSzamokOsszege(halmaz)
