"""Töltsünk fel egy listát a felhasználó által megadott elemű random számokkal:"""
from typing import *
import random
import os
import time

halmaz: List[int] = []
elemekSzama:int = None

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

#főprogram

elemekSzama= elemszamBekerese()
halmaz = ListaFeltoltesekRandomSzamokkal(elemekSzama)
os.system("cls")

print("A halamz elemei: \t")
halmazKiirasa(halmaz)


#Írassuk ki fordított sorrendben
print("\nA halmaz elemeinek kiírása fordított sorrendben: \t")
halmazKiirasaForditottSorrendben(halmaz)