print("x =")
x:int = int(input())

print("y =")
y:int = int(input())

print("z =")
z:int = int(input())

if(x > y > z):
    print(f"{z}, {y} {x}")
elif(x < y < z):
    print(f"{x}, {y}, {z}")
elif(x == y < z):
    print(f"(({x},{y}) or ({y},{x})),{z}")
elif(x == y > z):
    print(f"{z},{x},{y}")
elif(x == z > y):
    print(f"{y},{z},{x}")
elif(x == z < y):
    print(f"{x},{z},{y}")
elif(x < y == z):
    print(f"{x},{y},{z} or {x},{z},{y}")
elif(x > y == z):
    print(f"{y},{z},{x}, or {z},{y},{x}"):     
else:
    print(f"{x},{y},{z} egyenlőek")