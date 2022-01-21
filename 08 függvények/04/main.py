import os
import time

fok:float=None
atvaltasMertekegysege:str=None
atvaltottMennyiseg:float=None

#ho bekerese celsiusban

def hibaUzenet(hiba:str)->None:
    print(f"{hiba}")
    time.sleep(3)
    os.system("cls")

def homersekletBekerese()->float:
    eredmeny:float=None
    while (eredmeny==None):
        data:str=input("Kérem a hőmérsékletet C-ban: ")
        if(data.replace(".","").replace("-","").isdigit()):
            eredmeny=float(data)
            return eredmeny
        else:
            hibaUzenet("Nem számot adott meg!")

#megkerdezzuk, hogy farenheit vagy kelvinbe valtsa

def valtasValasztas()->str:
    eredmeny:str=None
    while(eredmeny==None):
        data:str=input("Kérem a véltás módját\n[K kelvin]\n[F farenheit]\n")
        if(data.capitalize()=="K" or data.capitalize()=="F"):
            eredmeny=data.capitalize()
            return eredmeny
        else:
            hibaUzenet("Nem opciót daott meg!")

#atvaltas

def valtas(celsius:float, mire:str)->float:
    if (mire=="K"):
        return celsius+273.15
    else:
        return 9/5 * celsius + 32

#kiiras

def kiiras(celsius:float, atvaltottFok:float, mertekegyseg:str)->None:
    print(f"{celsius}C = {atvaltottFok}{mertekegyseg}.")


#foprogram
celsius=homersekletBekerese()
atvaltasMertekegysege=valtasValasztas()
atvaltottMennyiseg=valtas(celsius, atvaltasMertekegysege)
kiiras(celsius, atvaltottMennyiseg, atvaltasMertekegysege)