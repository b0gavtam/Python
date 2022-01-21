bevitel: int = 0
korosztaly:int=0

while(korosztaly <= 0 or korosztaly > 99):
    bevitel= input("Kérem az életkorát:")
    if(bevitel.replace("-", "").isnumeric()):
        korosztaly = int(bevitel)
        if(korosztaly < 0 or korosztaly > 99):
            print("Nem adott meg megfelelő életkort")
    else:
        print("Nem számot adott meg")

if(korosztaly >= 0 and korosztaly <= 6):
    print("Ön gyerek.")
elif(korosztaly >= 7 and korosztaly <=18):
    print("Ön iskolás.")
elif(korosztaly >= 19 and korosztaly <=65):
    print("Ön dolgozó.")
else:
    print("ön nyugdíjas.")
