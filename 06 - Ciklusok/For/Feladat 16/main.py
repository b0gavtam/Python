parosSzamokOsszege:int = 0
paratlanSzamokOsszege:int = 0
atlag: float = 0

print("honnan")
kezdoErtek: int = int(input())

print("meddig")
vegErtek: int = int(input())

for i in range(kezdoErtek,vegErtek, 1):
    if(i % 2 == 0):
        parosSzamokOsszege+=1
    else:
        paratlanSzamokOsszege+=1
atlag = ((parosSzamokOsszege + paratlanSzamokOsszege)/ 2)
print(f"a páros és páratlan számok összegének átlaga: {atlag}")