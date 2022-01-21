parosSzamokOsszege:int = 0
paratlanSzamokSzorzata: int = 1

print("honnan")
kezdoErtek: int = int(input())

print("hová")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    if(i % 2 == 0):
        parosSzamokOsszege+=i
    else:
        paratlanSzamokSzorzata*=i

print(f"osszeg = {parosSzamokOsszege}")
print(f"szorzat = {paratlanSzamokSzorzata}")
            