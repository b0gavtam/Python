#11 – Írjunk programot amely a felhasználótól bekér egy páros majd egy tőlle nagyobb páratlan számot. A következő lépésben generáljunk egy véletlen számot e két érték közt és határozzuk meg mely szám (páros vagy páratlan) van messzebb a véletlen számunktól.
	 #Számítsuk ki a két bekért érték közti átlagot is.
	 #Számoljuk meg a 4-el osztható számok számát is.
     
import random

kezdoErtek:int = None
data1:str =""
vegErtek:int = None
data2:str= ""
rnd:int = 0

while(kezdoErtek == None or kezdoErtek % 2 == 1):
    data1 = input("Adja meg a kezdőértéket:")
    if(data1.replace("-", "").isnumeric()):
        kezdoErtek = int(data1)
    else:
        print("Nem számot adott meg")

while(vegErtek == None or vegErtek <= kezdoErtek or vegErtek % 2 == 0):
    data2 = input("Adja meg a végértéket:")
    if(data2.replace("-", "").isnumeric()):
        vegErtek = int(data2)     
    else:
        print("Nem számot adott meg")

rnd:int = random.randint(kezdoErtek, vegErtek)

for i in range(kezdoErtek, rnd+1, 1):
    if (abs(kezdoErtek -))