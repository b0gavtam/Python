elojelvalto:int=1
eredmeny:int=0

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek + 1, 1):
    eredmeny += i * elojelvalto
    elojelvalto = elojelvalto * (-1)

print(f"Az eredmény:{eredmeny}")