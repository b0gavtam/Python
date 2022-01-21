#9 – Kérjünk be egy 3 jegyű  számot és állapítsuk meg, hogy osztható e 7-el. Addig ismételjük a bekérést, amíg nem 3 jegyű a megadott szám.
szam:int = 0
data:str = ""

while(szam > 999 or szam < 100):
    data = input("Adjon meg egy háromjegyű számot:")
    if(data.replace("-", " ").isnumeric()):
        szam = int(data)
    if(szam > 999 or szam < 100):
        print("Nem Háromjegyű számot adott meg!")

if(szam % 7 == 0):
    print("Héttel osztható a szám")
else:
    print("Nem osztható 7-el a szám")