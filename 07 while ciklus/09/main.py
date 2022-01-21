import time
import os

data:str=""
number:int=0

while(number < 100 or number > 999):
    data=input("Adjon meg egy 3 jegyű számot")
    if(data.replace("-", "").isnumeric()):
        number=int(data)
        if (number < 100 or number > 1000):
            print("Csak háromjegyű számot adjon meg!")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

if(number % 7 == 0):
    print(f"A {number} szám osztható 7el")
else:
    print(f"A {number} szám nem osztható 7el")