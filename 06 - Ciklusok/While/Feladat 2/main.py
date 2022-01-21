#2 – Írjunk programot, amely bekéri a nevünket, és ha azt megadtuk, akkor üdvözlő szöveggel üdvözli a felhasználót.



#I: a név nem lehet üres string
#II: szóközök(egy vagy több)
#III: név hossza(min 3 karakter)
import os
import time

nev: str=""

while (nev == "" or nev.isspace() or len(nev) < 3):
    nev: str=str(input("Adja meg a nevét: "))
    
    if (nev == ""):
        print("Nem adott meg nevet!")
        time.sleep(3)
        os.system("cls")
        
    elif(nev.isspace()):
        print("Felesleges szóközöket írt!")
        time.sleep(3)
        os.system("cls")
        
    elif(len(nev) < 3):
        print("A név túl rövid!")
        time.sleep(3)
        os.system("cls") 

print(f"Üdvözöljük {nev}!")