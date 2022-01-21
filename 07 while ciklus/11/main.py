import random

data:str=""
kezdoErtek:int=None
vegErtek:int=None
neggyelOszthato:int=0

while (kezdoErtek==None or kezdoErtek % 2 != 0):
    data=input(("Kérek egy páros kezdőértéket: "))
    if(data.replace("-","").isnumeric()):
        kezdoErtek=int(data)
        if (kezdoErtek % 2 != 0):
            print("Páros értéket adjon meg!")

while(vegErtek == None or vegErtek % 2 == 0 or vegErtek< kezdoErtek):
    data=input(("Kérek egy páratlan végértéket: "))
    if(data.replace("-","").isnumeric()):
        vegErtek=int(data)
        if (vegErtek % 2 == 0):
            print("Páratlan értéket adjon meg!")
        if (kezdoErtek>vegErtek):
            print("A végértéknek nagyobbnak kellett lennie a végértéknél")

randomNumber=random.randint(kezdoErtek, vegErtek)
if(abs(randomNumber-kezdoErtek) < abs(randomNumber-vegErtek)):
    print(f"A {randomNumber} a kezdőértékhez ál közelebb")
elif(abs(randomNumber-kezdoErtek) > abs(randomNumber-vegErtek)):
    print(f"A {randomNumber} a végértékhez áll közelebb")
else:
    print(f"A {randomNumber} a két értéktől ugyanolyan távolságra van")

atlag:float=(kezdoErtek+vegErtek)/2
print(f"A számok átlaga: {atlag}")

for i in range(kezdoErtek, vegErtek + 1, 1):
    if (i % 4 == 0):
        neggyelOszthato+=1
print(f"{neggyelOszthato} db 4el osztható szám van a 2 között")