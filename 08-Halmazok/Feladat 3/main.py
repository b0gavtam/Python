"""3.Dobjunk egy dobókockával egymás után 7-szer, az eredményeket tároljuk el!
	Számoljuk ki a dobások átlagát
	Számoljuk meg hány hatos dobás történt
	Számoljuk meg hány dobás volt páratlan"""


from typing import *
import random


halmaz: List[int] = []
elemekSzama:int = random.randint(10,20)
osszeg:int = None
szam:int = None
paratlan:int = None
egy:int = 0
ketto:int = 0
harom:int = 0
negy:int = 0
ot:int = 0
hat:int = 0

def ListaFeltoltesekRandomSzamokkal(elem:int)-> List[int]:
    eredmeny: List[int] = []
    for i in range(elem + 1):
        eredmeny.append(random.randint(1,6))


def halmazKiirasa(kiirandoHalmaz:List[int])-> None:
    for szam in kiirandoHalmaz:
        print(f"{szam}", end="\t")


def paratlanSzamokSzama(kiirandoHalmaz:List[int])-> int:
    eredmeny:int = 0
    for item in range:
        if (item % 2 == 0):
            eredmeny+=1

def hatosokszama(kiirandoHalmaz:List[int])-> int:
    eredmeny:int = 0
    for item in kiirandoHalmaz:
        if (item == 6):
            eredmeny+=1

    return eredmeny            

#főprogram
halmaz = ListaFeltoltesekRandomSzamokkal(elemekSzama)
halmazKiirasa(halmaz)

osszeg = szamokOsszege(halmaz)
print(f"\nA számok átlaga: {osszeg / elemekSzama}")


paratlan = paratlanSzamokSzama(halmaz)
print(f"\nA páratlan számok száma: {paratlan}")
