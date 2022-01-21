harommaloszhatoSzamok:int=0

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek + 1, 1):
    if (i % 3== 0):
        harommaloszhatoSzamok+=1

print(f"Az intervallumban {harommaloszhatoSzamok} db 3mal osztató szám van")
 