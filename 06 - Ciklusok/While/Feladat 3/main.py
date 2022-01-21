#3 – A számítógép random generáljon egy számot 0 és 9 között. Majd a felhasználónak ki kell találni ezt a számot 5 nekifutásból.

import random

rnd:int = 0
tipp:int = 0
tippekSzama:int = 1
temp:str=""

rnd:int = random.randint(0, 9)

while(tipp != rnd and tippekSzama <= 5):

    temp="" 

    while(temp == "" or temp.isspace() or not temp.isnumeric()):
        temp = input(f"Kérem a(z) {tippekSzama}. tippet:")
        if(temp.isnumeric()):
            tipp = int(temp)
            tippekSzama+=1
        else:
            print("Nem számot adott meg tippnek.")

if(tipp == rnd):
    print(f"Gratulálunk, eltalálta a(z) {rnd} számot!")
else:
    print(f"Gratulálunk, nem találta el a(z) {rnd} számot!")
