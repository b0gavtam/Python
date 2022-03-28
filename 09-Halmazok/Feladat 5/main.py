"""5. Kérjük be egy dolgozó bruttó fizetését 12 hónapra. 
	Számoljuk ki mennyi SZJA –t fizet (az évi fizetés összegének 33,5%-a)
	Számoljuk ki mennyi egészségügyi hozzájárulást (SZJA 45%-a) és nyugdíjalapot fizetett (SZJA 55%-a )"""

from typing import *
import random

halmaz: List[int] = []
elemekSzama:int  = 12
honapok: Tuple[str] = (
    "Január",
    "Február",
    "Március",
    "Április",
    "Május",
    "Június",
    "Július",
    "Augusztus",
    "Szeptember",
    "Október",
    "November",
    "December",
)

fizetesek:List[int] = []
szjaErtek:float = None
tbErtek:float = None
nyugErtek:float = None




def fizetesekgeneralasa()-> List[int]:
    eredmeny:List[int]= []
    for i in range(0,12,1):
        eredmeny.append(random.randint(200, 1000))

    return eredmeny

def fizeteseKiirasa(berek:List[int], honapok:Tuple[str])-> None:
    for index in range(0,12,1):
        print(f"{honapok[index]} - {berek[index]}EUR")



def listaFeltolteseRandomSzamokkal(elem:int)-> List[int]:
    eredmeny: List[int] = []
    for i in range(elem + 1):
        eredmeny.append(random.randint(-100,100))

    return eredmeny

def evifizetes(berek:List[int])-> int:
    eredmeny: int = 0
    for item in berek:
        eredmeny+=item
    return eredmeny    

def SZJA(berek:List[int])-> float:
    osszeg: int = evifizetes(berek)
    return osszeg * 0.335


def TB(szja:float)-> float:
    return szja * 0.45

def nyugdij(szja:float)-> float:
    return szja * 0.55

#főprogram
halmaz = listaFeltolteseRandomSzamokkal(elemekSzama)
fizetesek = fizetesekgeneralasa()
fizeteseKiirasa(fizetesek, honapok)



szjaErtek = SZJA(fizetesek)
tbErtek = TB(szjaErtek)
nyugErtek = nyugdij(szjaErtek)
print(f"SZJA: {szjaErtek}EUR")
print(f"TB: {tbErtek}EUR")
print(f"Nyugdíjalap: {nyugErtek}EUR")


