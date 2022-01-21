print("Kérek egy számot")
x:int=int(input())

if(x>=0 and x<=9):
    print("egyjegyű szám")
elif(x>=10 and x<=99):
    print("kétjegyű szám")
elif(x>=100 and x<=999):
    print("háromjegyű szám")
else:
    print(f"{x} nem egyjegyű, kétjegyű vagy háromjegyű pozitív szám")