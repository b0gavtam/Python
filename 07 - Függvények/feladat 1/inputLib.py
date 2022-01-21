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