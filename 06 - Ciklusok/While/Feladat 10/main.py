#10- Kérjünk be egy max 2 jegyű, pozitív n számot:
#	Írjuk ki 0 és n közt a páros számokat
#	Adjuk össze 0 és n közt az 5-el osztható számokat
#	Számoljuk meg, hány szám osztható 0 és n közt 11-el
#	Írjuk ki azon számokat 0 és n közt amelyek 7-el osztva 3-at adnak maradékul
n:int = None
data:str = ""
szum:int = 0
tizenegyelOszthatoSzamok:int = 0

while(n == None or n > 99 or n < 0):
    data = input("Adjon meg egy egyjegyű vagy kétjegyű számot:")
    if(data.replace("-", " ").isnumeric()):
        n = int(data)
    if(n > 99 or n < 0):
        print("Nem egyjegyű vagy kétjegyű számot adott meg!")
for i in range(0, n+1, 1):
    if(i % 2 == 0):
        print(i, end=" ")
    if(i % 5 == 0):
        szum += i
    if(i % 11 == 0):
        tizenegyelOszthatoSzamok += 1

for i in range(0, n+1, 1):
        if(i % 7 == 3):
            print(f"\nA héttel osztható 3 maradékot adó számok: {i}") 

print(f"Az öttel osztható számok összege: {szum}")
print(f"A tizeneggyel osztható számok száma: {tizenegyelOszthatoSzamok}")