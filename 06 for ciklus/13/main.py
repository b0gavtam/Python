parosSzamokosszege:int=0
paratlanSzamokosszege:int=0

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek + 1, 1):
    if (i % 2== 0):
        parosSzamokosszege+=i
    else:
        paratlanSzamokosszege+=i

if (parosSzamokosszege > paratlanSzamokosszege):
    print("A páros számok össege nagyobb")
elif (parosSzamokosszege < paratlanSzamokosszege):
    print("A páratlan osztható számok össege nagyobb")
else:
    print("A páros és páratlan számok összege egyenlő")
 