kezdoErtek:int=int(input("Kérem a kezdő számot:"))
vegErtek:int=int(input("Kérem a vég számot:"))

for i in range(vegErtek, kezdoErtek-1, -1):
    print(i)
