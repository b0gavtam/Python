import datetime
import time
import os

nev:str=None
szuletesiEv:int=None
kor:int = None
#nev bekerese

def nevBekeres() -> str:
    a:str = None
    while (a == None):
        data:str = input("Kérem a nevét: ")
        if (len(data) < 3 ):
            print("Túl rövid nevet adott meg!")
            time.sleep(3)
            os.system("cls")
        else:
            a=data
            return a

#szuletesi ev bekerese

def szuletesiEvBeolvasas() -> int:
    szuletesiEv:int = None
    ma:datetime = datetime.datetime.now() #a mai dátumot adja vissza
    jelenlegiEv:int = int(ma.strftime("%Y")) #visszaadja a jelenlgi évet a változóba

    while (szuletesiEv == None):
        data=input("Kérem a születési dátumát: ")
        if(data.isdigit()):
            szuletesiEv=int(data)
            if(szuletesiEv >= jelenlegiEv):
                print("A születési év nem lehet nagyobb mint a jelenlegi év!")
                szuletesiEv=None
            else:
                return szuletesiEv
        else:
            print("nem számot adott meg!")
            time.sleep(3)
            os.system("cls")

#eletkor szamolas

def eletkorKiszamitasa(ev:int) -> int:
    ma:datetime = datetime.datetime.now()
    jelenlegiEv:int = int(ma.strftime("%Y"))
    
    return jelenlegiEv-ev

#kiiratas

def kiiratas(felhasznaloNev:str, ev:int):
    print(f"{felhasznaloNev} ön {ev} éves")

nev=nevBekeres()
szuletesiEv=szuletesiEvBeolvasas()

kor=eletkorKiszamitasa(szuletesiEv)

kiiratas(nev, kor)