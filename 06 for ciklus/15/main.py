eredmeny:int=0

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek + 1, 1):
    if (i % 2 != 0 and i % 3==0):
        eredmeny+=1

print(f"{eredmeny} db páratlan és 3al oszható szám van")