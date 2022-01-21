print("x =")
x:int = int (input())

if(x >= 0 and x <= 9):
    print("a szám egyjegyű")  
elif(x >= 10 and x <= 99):
    print("a szám kétjegyű")
elif(x >= 100 and x <= 999):
    print("a szám háromjegyű")
else:
    print("a szám nem háromjegyű és/vagy negatív")