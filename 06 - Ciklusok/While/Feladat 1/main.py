#1 – Kérjük meg a felhasználót, hogy adjon meg egy 0 – 9 közötti számot. Addig ismételjük amíg nem lesz jó a bevitel! Jó bevitel után írjuk ki ezt a számot a képernyőre

import os
import time

number:int=None
data:str=""

while(number==None or number < 0 or number > 9):
    data=input("Kérek egy számot 0 és 9 között: ")
    if(data.replace("-","").isnumeric()):
        number=int(data)
        if(number != None and (number < 0 or number > 9)):
            print("Nem megfelelő a szám (nincs 0 és 9 közt)")
            time.sleep(3)
            os.system("cls")
        else:
            print("Nem számot adott meg vagy a szám értéke nem 0 és 9 között van!")
            time.sleep(3)
            os.system("cls")
print(f"A beolvasott szám {number}")