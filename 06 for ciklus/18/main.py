szamokSzama:int=0
eredmeny:int=0

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek + 1, 1):
    szamokSzama+=1

    if (szamokSzama % 2 != 0):
        eredmeny+=i
    else:
        eredmeny-=i

print(f"Az eredmény:{eredmeny}")