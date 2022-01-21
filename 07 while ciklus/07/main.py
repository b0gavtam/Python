kisebb:int=None
nagyobb:int=None
data:str=""
lepesek:int=None

while (kisebb == None):
    data=input(("Kérem a kezdőértéket (kisebb szám)"))
    if (data.replace("-" , "").isnumeric()):
        kisebb=int(data)
    else:
        print("nem számot adott meg!")

while (nagyobb == None or nagyobb <= kisebb):
    data=input(("Kérem a végértéket (nagyobb szám)"))
    if (data.replace("-" , "").isnumeric()):
        nagyobb=int(data)
        if (kisebb >= nagyobb):
            print("A Nayobb érték nagyobb legyen a kissebbnél")        
    else:
        print("nem számot adott meg!")

while (lepesek==None or lepesek>(nagyobb-kisebb) or lepesek<=0):
    data=input(("Kérem a lépések számát"))
    if (data.replace("-" , "").isnumeric()):
        lepesek=int(data)
        if (lepesek>(nagyobb-kisebb)):
            print("A lépések száma nem lehet a 2 érték közötti számoknál nagyobb")        
        if (lepesek<=0):
            print("A lépések száma nem lehet 0 vagy negatív szám")
    else:
        print("nem számot adott meg!")

for i in range(nagyobb, kisebb-1, -lepesek):
    print(i, end="   ")