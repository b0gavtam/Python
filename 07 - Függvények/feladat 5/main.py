import os
import time

atvaltottForint: float = None

def hiba(szoveg:str)-> None:
    print(szoveg)
    time.sleep(2)
    os.system("cls")


def penzBekeres() -> float:
    eredmeny:float = None

    while(eredmeny == None):
        data:str = input("Kérem adjon meg egy összeget HUF-ban:")
        if(data.replace(".", "").replace("-", "").isdigit()):
            eredmeny= float(data)
            return eredmeny
        else:
            hiba("Nem jó a bemenő adat!")
            

def valtasValasztas()-> str:
    eredmeny: str = None

    while(eredmeny == None):
        data:str = input("Kérem a váltás módját: JPY - Japán yen, CHF - Svájci frank, USD - Amerikai dollár")
        if(data.upper() == "JPY" or data.upper() == "CHF" or data.upper() == "USD" ):
            eredmeny = data.upper()
            return eredmeny
        else:
            hiba("Ilyen opció nincs!")

def hufToEur(forint:float)-> float:
    return forint / 356.75

def atvaltas(forint:float, mire:str)-> float:
    euro: float = hufToEur(forint)
    
    if(mire == "JPY"):
        return eur * 0.75
    elif(mire == "CHF"):
        return forint * 0.55
    elif(mire == "USD"):
        return forint * 0.8   


def kiiras(forint:float,atvaltottForint:float, penznem:str)-> None:
    print(f"{forint}Ft = {atvaltottForint}{penznem} és {hufToEur(forint)} EUR.")

forint = penzBekeres()
penznem = valtasValasztas()
atvaltottForint = atvaltas(forint, penznem)
kiiras(forint, atvaltottForint, penznem)


