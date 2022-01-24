import os
import time

def hiba(uzenet:str)->None:
    print(uzenet)
    time.sleep(2)
    os.system("cls")

#pontszám bekérése
def pontBekerese()-> int:
    pontszam: int = None
    while(pontszam == None):
        data:str=input("Kérem adjon meg egy pontszámot 0 és 100 között: ")
        if(data.isdigit()):
            pontszam = int(data)
            if(int(data) <= 100 and int(data) >= 0 ):
                return pontszam
            else:
                pontszam = None
                hiba("0 és 100 között adjon meg értéket!")
                
        else:
            hiba("Nem számot adott meg!")
#pontszám vizsgálata
def pontVizsgalata(pontszam:int)-> int:
    if(pontszam < 50):
        return 1
    elif(pontszam >=50 and pontszam < 60):
       return 2
    elif(pontszam >=60 and pontszam < 70):
        return 3    
    elif(pontszam >=70 and pontszam < 85):
        return 4
    else:
        return 5  
#kiírás
def kiírás(pontszam:int, osztalyzat:int)-> None:
    print(f"{pontszam} pontszámra {osztalyzat} érdemjegyet ért el.")
#főprogram

pontszam:int = pontBekerese()
osztalyzat:int = pontVizsgalata(pontszam)
kiiras(pontszam, osztalyzat)