szamokSzama:int=0
szamokOsszege:int=0

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek + 1, 1):
    szamokOsszege+=i
    szamokSzama+=1
        
eredmeny:float=szamokOsszege / szamokSzama
print(f"Az átlag:{eredmeny}")