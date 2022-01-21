parosSzamokOsszege:int = 0
paratlanSzamokOsszege:int = 0

print("honnan")
kezdoErtek: int = int(input())

print("meddig")
vegErtek: int = int(input())

for i in range(kezdoErtek,vegErtek, 1):
    if(i % 2 == 0):
        parosSzamokOsszege+=1
    else:
        paratlanSzamokOsszege+=1
        
if(parosSzamokOsszege < paratlanSzamokOsszege):
    print("A páratlan számok összege a nagyobb")
elif(parosSzamokOsszege > paratlanSzamokOsszege):
    print("A páros számok összege a nagyobb")
else:
    print("Ugyanannyi a páros és páratlan számok száma")    