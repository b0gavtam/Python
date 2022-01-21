print("Kérem az 1. számot")
x:float=float(input())

print("Kérem a 2. számot")
y:float=float(input())

osszeg:float=x+y

print("Kérem a 3. számot")
z:float=float(input())

print("Kérem a 4. számot")
a:float=float(input())
kulombseg:float=z-a

eredmeny:float=osszeg/kulombseg
print(f"{x} + {y} = {osszeg}")
print(f"{z} - {a} = {kulombseg}")
print(f"{osszeg} / {kulombseg} = {eredmeny}")