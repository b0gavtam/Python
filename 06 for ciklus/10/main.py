sum:int=0 
szorzat:int=1

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek+1, 1):
    sum+=i
    szorzat = szorzat * i

print(f"A számok össezge {sum}, a szorzatuk {szorzat}")