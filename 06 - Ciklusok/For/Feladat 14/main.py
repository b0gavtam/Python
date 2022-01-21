ottelOszthatoSzamokOsszege:int = 0
hettelOszthatoSzamokOsszege:int = 0

print("honnan")
kezdoErtek: int = int(input())

print("meddig")
vegErtek: int = int(input())

for i in range(kezdoErtek,vegErtek, 1):
    if(i % 5 == 0 and i % 7 == 0):
        ottelOszthatoSzamokOsszege+=1
        hettelOszthatoSzamokOsszege+=1
    elif(i % 7 == 0):
        hettelOszthatoSzamokOsszege+=1
    elif(i % 5 == 0):
        ottelOszthatoSzamokOsszege+=1
        
if(ottelOszthatoSzamokOsszege < hettelOszthatoSzamokOsszege):
    print("A héttel osztható számok összege a nagyobb")
elif(ottelOszthatoSzamokOsszege > hettelOszthatoSzamokOsszege):
    print("A héttel osztható számok összege a nagyobb")
else:
    print("Ugyanannyi az öttel és héttel osztható számok száma")    