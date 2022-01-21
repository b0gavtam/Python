osszeg:int = 0
szamokSzama:int = 0
atlag: float = 0

print("honnan")
kezdoErtek: int = int(input())

print("meddig")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek, 1):
    szamokSzama+=1
    osszeg+=i

atlag = osszeg / szamokSzama
print(f"az intrvallum átlaga: {atlag}")