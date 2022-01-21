kezdoErtek:int=int(input("Kérem a kezdőértéket:"))
vegErtek:int=int(input("Kérem a végértéket:"))

if (kezdoErtek % 2 == 0):
    kezdoErtek+=1

for i in range(kezdoErtek, vegErtek+1, 2):
    print(i)
