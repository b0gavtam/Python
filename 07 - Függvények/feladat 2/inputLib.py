def tizedesSzamBeolvasasa(a:str)->float:
    szam:float=None
    while(szam==None):                                                          #számbeolvasás függvény, ami amíg none a szám, ismétel, majd ha nem, akkor a számot átvariálja, behelyettesíti a változóba
        beolvasottSzam=input(f"{a}")
        if(beolvasottSzam.replace("-","").replace(".","").isdigit()):
            number=int(beolvasottSzam)
            return number
        else:
            print("Nem számot adott meg!")

def egeszSzamBeolvasasa(a:str)->int:
    szam:int=None
    while(szam==None):                                                          #számbeolvasás függvény, ami amíg none a szám, ismétel, majd ha nem, akkor a számot átvariálja, behelyettesíti a változóba
        beolvasottSzam=input(f"{a}")
        if(beolvasottSzam.replace("-","").replace(".","").isdigit()):
            number=int(beolvasottSzam)
            return number
        else:
            print("Nem számot adott meg!")


def nevBekeres()->str:
    nev:str = None

    while(nev==None):
        data:str = input("Kérem a nevét:")

        if(len(data) < 3): #len = length
            print("Túl rövid a név, minimum 3 karakter")
            time.sleep(2)
            os.system("cls")
        else:
            nev = data

    return nev