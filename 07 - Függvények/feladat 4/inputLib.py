#tizedesszám kiírása
def tizedesSzamBeolvasasa(a:str)->float:
    szam:float=None
    while(szam==None):                                                          #számbeolvasás függvény, ami amíg none a szám, ismétel, majd ha nem, akkor a számot átvariálja, behelyettesíti a változóba
        beolvasottSzam=input(f"{a}")
        if(beolvasottSzam.replace("-","").replace(".","").isdigit()):
            number=int(beolvasottSzam)
            return number
        else:
            print("Nem számot adott meg!")

#egész szám beolvasása
def egeszSzamBeolvasasa(a:str)->int:
    szam:int=None
    while(szam==None):                                                          #számbeolvasás függvény, ami amíg none a szám, ismétel, majd ha nem, akkor a számot átvariálja, behelyettesíti a változóba
        beolvasottSzam=input(f"{a}")
        if(beolvasottSzam.replace("-","").replace(".","").isdigit()):
            number=int(beolvasottSzam)
            return number
        else:
            print("Nem számot adott meg!")

#név bekérése
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

#születési év bekérése
def szuletesiEvBekerese()-> int:
    eredmeny:int=None
    ma:datetime = datetime.datetime.now()#a  mai dátumot adja vissza
    jelenlegiEv:int = int(ma.strftime("%Y")) #visszaadja a jelenlegi évet a  dátumból
    while(eredmeny == None):
        data:str=input("Kérem adja meg a születési évét:")
        if(data.replace("-", "").isnumeric()):
            eredmeny = int(data)

            if(eredmeny >=jelenlegiEv):
                eredmeny==None
                print("A születési év nem lehet nagyobb, mint a jelenlegi év!")
                time.sleep(2)
                os.system("cls")

            return eredmeny
        else:
            print("Nem számot adott meg!")
            time.sleep(2)
            os.system("cls")

#életkor kiszámítása
def eletkorKiszamitasa(szuletesiEv:int)-> int:
    ma:datetime = datetime.datetime.now()#a  mai dátumot adja vissza
    jelenlegiEv:int = int(ma.strftime("%Y")) #visszaadja a jelenlegi évet a  dátumból

    return jelenlegiEv - szuletesiEv                