import os
import time

def pontSzamBeolvasasa(a:str)->int:
    pont:int=None
    while(szam==None):
        beolvasottSzam=input(f"{a}")
        if(beolvasottSzam.replace("-","").replace(".","").isdigit()):
            number=int(beolvasottSzam)
            return number
        else:
            print("Nem számot adott meg!")