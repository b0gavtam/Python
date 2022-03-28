"""1. egész szám bekérése függvény
   2. számok bekérése
        -addig fut, amíg 3 olyan számot nem adunk meg, amely nem szerepelt még a listában
"""
from typing import *
halmaz:List[int] = []



def szamBeolvasasa()-> int:
    eredmeny:int = None
    data:str = None
    
    while(eredmeny == None):
        data = input("Kérem adjon meg egy számot: ")
        if(data.isdigit()):
            eredmeny = int[data]
        else:
            print("Nem számot adott meg!")
            
            
    return eredmeny

def listaFeltoltese()-> List[int]:
    lista: List[int] = []
    ujElemekSzama:int = 0
    szam:int = None
    
    while(ujElemekSzama <= 3): #
        szam = szamBeolvasasa()
        #megvizsgálja, hogy a szám szerepel-e a listában
        letezikE = True if(lista.count(szam) == 1) else False
        
        
        #ha a szám nem létezik, hozzáadja a listához
        if(not letezikE):
            lista.append(szam)
            ujElemekSzama +=1
        #ha már benne van a listában, akkor nem új elem, újraindítja
        else:
            ujElemekSzama = 0    
            print(f"{szam} mar szerepel a listában.")
        
    return lista


halmaz:List[int] = listaFeltoltese()
print(halmaz)




            
