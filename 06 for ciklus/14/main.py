ottelOszthatoSzamokOsszege:int=0
hettelOszthatoSzamokOsszege:int=0

kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

for i in range(kezdoErtek, vegErtek + 1, 1):
    if (i % 5== 0):
        ottelOszthatoSzamokOsszege+=i

    if(i % 7 == 0):
        hettelOszthatoSzamokOsszege+=i

if (ottelOszthatoSzamokOsszege > hettelOszthatoSzamokOsszege):
    print("Az öttel osztható számok össege nagyobb")
elif (ottelOszthatoSzamokOsszege < hettelOszthatoSzamokOsszege):
    print("A héttel osztható számok össege nagyobb")
else:
    print("Az öttel és héttel oszható számok összege egyenlő")
 