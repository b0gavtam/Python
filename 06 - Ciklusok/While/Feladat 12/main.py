#12 - Van egy kis megtakarított pénzem (min 10.000, max 50.000). Arra vagyok kíváncsi, hogy hány hónap múlva éri el ez az összeg a bankban a 100 000 Ft-ot, ha havi 2%-os kamattal számolhatok?
penz:float = None
data:str =""
honapokSzama:int = 0

while( penz == None or  penz > 50000 or penz < 10000):
    penz = input("Adjon meg egy pénzmennyiséget 10000 és 50000 között:")
    if(data.isnumeric):
        penz = float(data)
    else:
        print("Nem adott meg jó számot!")

while(penz < 100000):
    penz = penz * 1.02
    honapokSzama+=1
print(f"Ennyi hónap elteltével éri el a százezret 2% kamattal: {honapokSzama}")