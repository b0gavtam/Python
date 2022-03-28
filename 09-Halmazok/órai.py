from typing import *
import random

szabi:List[int] = []
nevek:List[str]= []

def szabadnapok()->List[int]:
    eredmeny:List[int] = []
    eredmeny2:int = None
    while(eredmeny2 == None or len(eredmeny) < 10):
        for i in range(0,10,1):
        data:str = input("Adja meg az éves szabadnapjainak értékét: ")
            if(data.isdigit()):
                eredmeny2 = int(data)
                eredmeny.append(eredmeny2)
            else:
                print("nem számot adott meg!")


    return eredmeny

def nev(szabadnapok:List[int])->List[str]:
    eredmeny:List[str] = []
    emberek:int  = 0
    while(emberek < 10):
        data:str = input(f"Adja meg a nevét {szabadnapok[i+1]} értéknek: ")
        if(data.isdigit):
            print("Nevet adjon meg!")
        else:
            eredmeny.append(data)
            emberek+=1
    
    
    return eredmeny            



szabi = szabadnapok()
print(szabi)
nevek = nev(szabi)




