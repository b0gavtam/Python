#Írjunk programot, amelyben a felhasználó megad egy határértéket (min 100), majd a felhasználótól addig kér be számokat, még azok összege nem haladja meg a határértéket. Minden bekérés után jelezni a felhasználónak a jelenlegi összeget.  Ha az összeg eléri a határértéket akkor kiírni, hány lépésben érte el a felhasználó azt.
szumInput: str = ""
inputText:str =""
number:int = 0
proba:int = 0
osszeg:int = None
szum:int = 0

while(osszeg == None or osszeg < 100):
    szumInput = input("Kérem a határétéket:")
    if(szumInput.replace("-", "").isnumeric()):
        osszeg = int(szumInput)
        if(osszeg < 100):
            print("A határérték nem lehet kisebb 100-nál")
    else:
        print("Nem számot adott meg")

while(szum < osszeg):
    inputText = input("Kérek egy számot: ")
    if(szumInput.replace("-", "").isnumeric()):
        number = int(inputText)
        szum += number
        proba += 1
        print(f"Az eddigi számok összege: {szum}")
    else:
        print("Nem számot adott meg")

print(f"A végső érték {szum}, ennyi szám után: {proba}")