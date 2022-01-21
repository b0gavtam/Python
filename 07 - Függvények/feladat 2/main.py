import os
import time
from inputLib import *

def nevBekeres()->str:
    nev:str = None

    while(nev==None):
        data:str = input("Kérem a nevét:")

        if(len(data) < 3): #len = length
            print("Túl rövid a név, minimum 3 karakter")
            time.sleep(2)
            os.system("cls")
        else:
            nev = data

    return nev

def udvozles(nev:str)-> None
    print(f"Üdvözöljük {nev}!")

felhasznalo:str=nevBekeres()
udvozles(felhasznalo)