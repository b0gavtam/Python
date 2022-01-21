import os
import time
# Írj egy mértékegység konvertáló programot. Az átalakítást Celsius-ból függvénnyel oldjuk meg amely két paramétert kap! Az első egy hőmérséklet érték, a második paraméter pedig azt jelzi milyen mértékegységre akarjuk átkonvertálni (’F’: Fahrenheit, ’K’: Kelvin). 
#(K = C+273,15; F = 9/5*C+32).
#Egyes logikai egészeket alkotó műveleteket függvényekkel oldjuk meg.

celsius:float = None
atvaltasMertekegysege: str = None
atvaltottMennyiseg: float = None

#hiba kírása mert a hibaüzenet ugyanazon ismétlődő kód
def hiba(szoveg:str)-> None:
    print(szoveg)
    time.sleep(2)
    os.system("cls")   

#1 hőmérséklet bekérése celsiusban
def homersekletBekerese() -> float:
    eredmeny:float = None

    while(eredmeny == None):
        data:str = input("Kérem adja meg a hőmérsékletet Celsiusban:")
        if(data.replace(".", "").replace("-", "").isdigit()):
            eredmeny= float(data)
            return eredmeny
        else:
            hiba("Nem jó a bemenő adat!")
            

#2 F vagy K legyen a váltás módja
def valtasValasztas()-> str:
    eredmeny: str = None

    while(eredmeny == None):
        data:str = input("Kérem a váltás módját [Fahrenheit vagy Kelvin]:")
        if(data.capitalize() == "K" or data.capitalize() == "F" ):
            eredmeny = data.capitalize()
            return eredmeny
        else:
            hiba("Ilyen opció nincs!")



#3 átváltás
def atvaltas(fokCelsius:float, mire:str)-> float:
    if(mire == "K"):
        return fokCelsius + 273.15
    elif(mire == "F"):
        return 9 / 5 * fokCelsius + 32




#4 kiírás
def kiiras(fokCelsius:float,atvaltottFok:float, mertekegyseg:str)-> None:
    print(f"{fokCelsius}C = {atvaltottFok}{mertekegyseg}.")



#főprogram
celsius= homersekletBekerese()
atvaltasMertekegysege = valtasValasztas()
atvaltottMennyiseg = atvaltas(celsius, atvaltasMertekegysege)
kiiras(celsius, atvaltottMennyiseg, atvaltasMertekegysege)

#hála istennek legalább ez működik
#hétfőig va emailjére kell elküldeni az ikt-t(krétában elméletileg benne van)