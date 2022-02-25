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
hat:int = None
dic:Dict[int,int]

def listaFeltoltesekRandomSzamokkal(elem:int)-> List[int]:
    eredmeny: List[int] = []
    for i in range(elem + 1):
        eredmeny.append(random.randint(1,6))

    return eredmeny

def halmazKiirasa(kiirandoHalmaz:List[int])-> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")

def szamokOsszege(kiirandoHalmaz:List[int])-> int:
    eredmeny:int = 0
    for item in kiirandoHalmaz:
        eredmeny+=item
    
    return eredmeny

def paratlanSzamokSzama(kiirandoHalmaz:List[int])-> int:
    eredmeny:int = 0
    for item in kiirandoHalmaz:
        if (item % 2 == 0):
            eredmeny+=1

    return eredmeny

def hatosokszama(kiirandoHalmaz:List[int])-> int:
    eredmeny:int = 0
    for item in kiirandoHalmaz:
        if (item == 6):
            eredmeny+=1

    return eredmeny            



"""
def legtobbszam(kiirandoHalmaz:List[int])-> Dict[int,int]:
    dict:Dict[int,int]
    for item in kiirandoHalmaz:
        if(dict.has_key(szam)):
            dict[szam]+1
        else:
            dict.add(szam,1)
    
    return dict
"""

def legnagyobbKulcsErteke(szotar: Dict[int, int])-> List[int]:
    kulcs:int = None
    ertek:int = 0
    eredmeny:List[int]=[]

    #a legnagyobb érték kikeresése a szótárból
    for key, value in szotar.items(): #végiglépkedünk a szótár összes elemén kulcs-érték párokkal
        if (szotar[key] > ertek):
            kulcs = key
            ertek = szotar[key]

    #kikeressük azokat a kulcsokat, amelyek értéke egyenlő az érték változóval, 
    # mivel azoknak a kulcsoknak a száma fordul elő a legtöbbször
    for key, value in szotar.items(): 
        if(szotar[key] == ertek):
            eredmeny.append(key)


    return eredmeny


def legtobbetEloforduloSzam(lista:List[int])-> List[int]:
    szotar: Dict[int, int] = {} #Dict[kulcs-> szám, value -> szám előfordulási száma]
 
    #meghatározzuk az előfordulási számokat
    for szam in lista:
        if(szam in szotar):
            szotar[szam]+=1 #szotar[szam] -> a kulcshoz tartozó értéket adja vissza
        else:
            szotar[szam] = 1

    #lista = [2,4,1,1,6,3,1]
    #szotar = {1:3, 2:1, 3:1, 4:1, 6:1}

    eredmeny: List[int] = legnagyobbKulcsErteke(szotar)
    return eredmeny

#főprogram
halmaz = listaFeltoltesekRandomSzamokkal(elemekSzama)
halmazKiirasa(halmaz)

osszeg = szamokOsszege(halmaz)
print(f"\nA számok átlaga: {osszeg / elemekSzama}")

paratlan = paratlanSzamokSzama(halmaz)
print(f"\nA páratlan számok száma: {paratlan}")

hat = hatosokszama(halmaz)
print(f"\nHatos dobások száma: {hat} ")

legtobbetEloforduloszamok:List[int] = legtobbetEloforduloSzam(halmaz)
print(f"A legtöbbet előforduló szám(ok): ")
print(legtobbetEloforduloSzam)