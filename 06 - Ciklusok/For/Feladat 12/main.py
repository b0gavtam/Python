harommalOszthatoSzamokSzama: int = 0

print("honnan")
kezdoErtek: int = int(input())

print("meddig")
vegErtek: int = int(input())

for i in range(kezdoErtek,vegErtek, 1):
    if(i % 3 == 0):
        harommalOszthatoSzamokSzama+=1
    
print(f"Hárommal osztható számok száma = {harommalOszthatoSzamokSzama}")