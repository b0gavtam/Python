print("kérek egy számot")
x:int=int(input())

if (x % 2 == 0):
    print(f"{x} páros")
else:
    print(f"{x} páratlan")

if (x>0):
    print(f"{x} pozitív")
elif(x<0):
    print(f"{x} negatív")
else:
    print(f"{x} 0")

if (x%5==0):
    print(f"{x} osztható 5el")
else:
    print(f"{x} nem osztható 5el")