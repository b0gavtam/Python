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
legtobb:int = 0
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


def paratlanSzamokSzama(kiirandoHalmaz:List[int])-> int
    eredmeny:int = 0
    for item in range:
        if (item % 2 == 0):
            eredmeny+=1

def legtobbszam(kiirandoHalmaz:List[int])-> int:

    for i in kiirandoHalmaz:
        if(i == 1):
            egy+=1
        elif(i == 2):
            ketto+=1
        elif(i == 3):
            harom+=1
        elif(i == 4):
            negy+=1
        elif(i == 5):
            ot+=1
        elif(i == 6):
            hat+=1


    return legtobbszam



#főprogram
halmaz = ListaFeltolteseRandomSzamokkal(elemekSzama)
halmazKiirasa(halmaz)

osszeg = szamokOsszege(halmaz)
print(f"\nA számok átlaga: {osszeg / elemekSzama}")

