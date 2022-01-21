paratlanSzamokOsszege:int=0
parosSzamokOsszege:int=0

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek + 1, 1):
    if (i % 2 == 0):
        parosSzamokOsszege+=i
    else:
        paratlanSzamokOsszege+=i
        
eredmeny:float=(parosSzamokOsszege + paratlanSzamokOsszege) / 2
print(f"Az átlag:{eredmeny}")