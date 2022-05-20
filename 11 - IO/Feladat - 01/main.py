from diak import Diak
from typing import *
from diakio import *
from osztaly import *


diakok: List[Diak] = DiakIO.read("adatok.txt")

#diákok adatai
print("A diakok adatai: \n")
for diak in diakok:
    print(f"{diak}\n")
    
#hány diák
print(f"az osztályba {len(diakok)} diák jár.")

#osztályátlag
atlag:float = Osztaly.atlag(diakok)
print(f"az osztály átlaga: {atlag:1.2f}")

#legmagasabb átlagúak
joDiakok:List[Diak]= Osztaly.legjobbak(diakok)
for diak in joDiakok:
    print(f"A legmagasabb átlaggal rendelkező diák: {diak}")

#átlagfeletti tanulók kiírása atlagfelettiek.txt-be
Osztaly.atlagfelettiek(diakok, atlag)

#van e kitűnő tanuló(nincs)
van:bool = Osztaly.vanekitunotanulo(diakok)
if(van):
    print(f"van kitűnő tanuló")
else:
    print("nincs kitűnő tanuló")

#hány elégtelen elégséges, jó,jeles kitűnő  0.00 - 1.99,2.00 2.99    
"""elegtelen: List[Diak] = []
elegseges: List[Diak] = []
jo: List[Diak] = []
jeles: List[Diak] = []
kituno: List[Diak] = []


Osztaly.besorolas(diakok, elegtelen, elegseges, jo, jeles, kituno)

print(f"Elégtelen tanulók száma: {len(elegtelen)}\nElégséges tanulók száma: {len(elegseges)}\nJó tanulók száma: {len(jo)}\nJeles tanulók száma: {len(jeles)}\nKitünő tanulók száma: {len(kituno)}")"""

besorolas:Dict[str,int] = Osztaly.besorolas(diakok)
for(key,value) in besorolas.items():
    print(f"\t- {key} : {value}\n")