print("x:")
x:int=int(input())

print("y:")
y:int=int(input())

print("z:")
z:int=int(input())

if(x % y == 0 and x % z == 0):
    print(f"{x} osztható {y}el és {z}el")
elif(x % y == 0):
    print(f"{x} osztható {y}al")
elif(x % z == 0):
    print(f"{x} oszthazó {z}el")
else:
    print(f"{x} nem osztható {y}el se és {z}el se")