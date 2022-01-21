kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

if (vegErtek % 2 != 0):
    vegErtek-=1

for i in range(vegErtek, kezdoErtek-1, -2):
    print(i)