print("kérek egy számot")
x:int=int(input())

print("kérek egy másik számot")
y:int=int(input())

if(x>y):
    print(f"{x}")
elif(x<y):
    print(f"{y}")
else:
    print(f"{x} és {y} egyenlő")