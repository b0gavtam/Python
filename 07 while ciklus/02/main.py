import os
import time

nev:str=""

while(nev == "" or nev.isspace() or len(nev) < 3):
    nev:str=str(input("Kérem a nevét: "))
    if (nev == "" ):
        print("Nem adott meg nevet!")
        time.sleep(3)
        os.system("cls")
    elif(nev.isspace()):
        print("Csak szóközt adott meg névnek!")
        time.sleep(3)
        os.system("cls")
    elif(len(nev) < 3):
        print("Túl rövid nevet adott meg!")
        time.sleep(3)
        os.system("cls")
    
print(f"Üdvözöljük {nev}!")