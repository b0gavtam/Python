parosSzamokOsszege:int=0
paratlanSzamokszorzata:int=1

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek + 1, 1):
    if i % 2== 0:
        parosSzamokOsszege+=i
    else:
        paratlanSzamokszorzata*=i  

print(f"A páros számok összege: {parosSzamokOsszege}.")
print(f"A páratlan számok szorzata: {paratlanSzamokszorzata}.")