import random

rnd:int=random.randint(0, 9)
probak:int=1
tipp:int=0
bevitel:str=""

while(tipp != rnd and probak <=5):
    bevitel=input(f"Kérem a {probak}. tippjét:")
    if (bevitel.isdigit()):
        tipp=int(bevitel)
        probak+=1     
    else:
        print("Nem számot adott meg!")

if(tipp == rnd):
    print(f"Eltalálta a {rnd} számot {probak - 1} próba alatt")
else:
    print("Kifogyott a próbálkozásból")