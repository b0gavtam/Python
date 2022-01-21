elojelvalto:int = 1
osszeg:int = 0
szamokSzama:int = 0

print("honnan")
kezdoErtek: int = int(input())

print("meddig")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    osszeg=osszeg+i*elojelvalto

    elojelvalto = elojelvalto*(-1)
print(f"{osszeg}")