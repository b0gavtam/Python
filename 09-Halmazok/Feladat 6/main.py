from typing import *
import random
import os
import time

halmaz1: List[int] = []
halmaz2: List[int] = []
osszeg:int = 0

def szamBeolvasasa(mini:int, maxi:int)-> int:
    eredmeny:int  = None
    while(eredmeny == None or eredmeny<mini or eredmeny>maxi):
        data:str=input("Kérem adja meg az elemek számát: ")
        if(data.isdigit()):
            eredmeny = int(data)
            if(eredmeny>maxi or eredmeny<mini):
                print("Nem határértéken belüli számot adott meg!")
        else:
            print("Nem számot adott meg!")
            time.sleep(2)
            os.system("cls")

    return eredmeny

def listaFeltolteseRandomSzamokkal(elem:int)->List[int]:
    eredmeny: List[int] = []
    for i in range(elem + 1):
        eredmeny.append(random.randint(-100,100))

    return eredmeny


def halmazKiirasa(kiirandoHalmaz:List[int])-> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")

def halmazKiirasa2(kiirandoHalmaz:List[int])-> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")

def novekvosorrendukiiras(keresesHalmaza:List[int])-> List[int]:
    temp:int = None
    for i in range(0, len(keresesHalmaza), 1):
        for j in range(i + 1, len(keresesHalmaza), 1):
            if(keresesHalmaza[j] < keresesHalmaza[i]):
                temp = keresesHalmaza[i]
                keresesHalmaza[i] = keresesHalmaza[j]
                keresesHalmaza[j] = temp
    return keresesHalmaza

def osszeadas(keresesHalmaza:List[int])-> int:
    osszeg: int = 0
    for item in keresesHalmaza:
        osszeg+=item

    return osszeg    

"""def listaosszefuzes(halmaz1:List[int], halmaz2:List[int])->List[int]:
    eredmeny:List[int]=halmaz1.copy()
    for item in halmaz2:
        eredmeny.append(item)

    megoldás 2
    eredmeny:List[int]=halmaz1.copy()
    eredmeny += halmaz2.copy()
    
    return eredmeny
"""
#főprogram
elemszam = szamBeolvasasa(1,5)
halmaz1 = listaFeltolteseRandomSzamokkal(elemszam)
elemszam2 = szamBeolvasasa(5,10)
halmaz2 = listaFeltolteseRandomSzamokkal(elemszam2)
halmazKiirasa(halmaz1)
halmazKiirasa2(halmaz2)
novekvosorrend: List[int] = novekvosorrendukiiras(halmaz1+halmaz2)
print(f"\n A halmaz növekvő sorrendben: {novekvosorrend}")
osszeg = osszeadas(halmaz1+halmaz2)
print(f"A halmaz átlaga: {osszeg/(elemszam+elemszam2)}")