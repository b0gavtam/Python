print("Kérem az 1. számot")
x:float=float(input())

print("Kérem a 2. számot")
y:float=float(input())

print("Kérem a 3. számot")
z:float=float(input())

osszeg:float=x+0.5
kulombseg:float=y-0.7
eredmeny:float=(osszeg*kulombseg) % z

print(f"Az eredmény {eredmeny}")