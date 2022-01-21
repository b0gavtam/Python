import time
import os

data:str=""
number:int=None
ottelOszthatoSzum:int=0
tizeneggyelOszthatokSzama:int=0

while(number == None or number < 0 or number > 99):
    data=input("Adjon meg egy maximum 2 jegyű számot: ")
    if(data.replace("-", "").isnumeric()):
        number=int(data)
        if (number < 0 or number > 99):
            print("Maximum kétjegyű pozitív számot adjon meg!")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

print("A 2vel osztható számok:")
for i in range(0, number + 1, 1):
    if(i % 2 == 0):
        print(i, end=",  ")
    if(i % 5 == 0):
        ottelOszthatoSzum+=i
    if(i % 11 == 0):
        tizeneggyelOszthatokSzama+=1

print(f"\nAz 5el osztható számok összege:{ottelOszthatoSzum}\n11 el osztható számok száma:{tizeneggyelOszthatokSzama}")
print("A 7el osztva 3 maradékot adó számok:")

for i in range(0, number + 1, 1):
    if(i % 7 == 3):
        print(i, end=",  ")