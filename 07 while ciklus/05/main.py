hatarErtekInput:str=""
inputtext:str = ""
number:int = 0
proba:int = 0
osszeg:int= 0
hatarErtek:int=0

while(hatarErtek < 100):
    hatarErtekInput=input("Mit szeretne hatarértéknak megadni: ")
    if(hatarErtekInput.replace("-", "").isnumeric()):
        hatarErtek=int(hatarErtekInput)
        if (hatarErtek < 100):
            print("Minimum 100 lehet a hatarérték")
    else:
        print("Nem számot adott meg!")
print(f"Megadta a {hatarErtek} számot összegnek")

while(osszeg < hatarErtek):
    inputtext=input("Kérek egy számot:")
    if(inputtext.replace("-", "").isnumeric()):
        number=int(inputtext)
        osszeg += number
        proba+=1
        print(f"Az eddigi számok összege: {osszeg}, a bevitelek száma {proba}")
    else:
        print("Nem számot adott meg!")
print(f"A végső érték: {osszeg}, {proba} próbálkozás után")