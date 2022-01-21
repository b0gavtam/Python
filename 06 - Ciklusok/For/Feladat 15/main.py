eredmeny: int = 0

print("honnan")
kezdoErtek: int = int(input())

print("meddig")
vegErtek: int = int(input())

for i in range(kezdoErtek, vegErtek, 1):
    if(i % 2 == 1 and i % 3 == 0):
        eredmeny+=1
print(f"Hárommal osztható páratlan számok száma: {eredmeny}")