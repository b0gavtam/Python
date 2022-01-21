import time
import os

def nevBekeres() -> str:
    nev:str=None
    while (nev == None):
        data:str =input("kérem a nevét: ")
        if (len(data) < 3 ):
            print("Túl rövid nevet adott meg!")
            time.sleep(3)
            os.system("cls")
        else:
            nev=data
    return nev

def tizedesSzamBeolvasas(a:str) -> float:
    number:float=None
    while(number==None):
        beolvasottSzam=input(f"{a}")
        if(beolvasottSzam.replace("-","").replace(".","").isdigit()):
            number=float(beolvasottSzam)
            return number
        else:
            print("nem számot adott meg!")

def egeszSzamBeolvasas(a:str) -> int:
    number:int=None
    while(number==None):
        beolvasottSzam=input(f"{a}")
        if(beolvasottSzam.replace("-","").isdigit()):
            number=int(beolvasottSzam)
            return number
        else:
            print("nem számot adott meg!")

