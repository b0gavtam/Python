eletkor:int=None
korInput:str=""

while(eletkor == None or eletkor < 0 or eletkor > 99):
    korInput=input("Mi az életkora: ")
    if(korInput.replace("-", "").isnumeric()):
        eletkor=int(korInput)
        if (eletkor > 99 or eletkor < 0):
            print("Minimum 0, maximum 99 lehet életkora!")
    else:
        print("Nem számot adott meg!")

print(f"Az ön életkora: {eletkor}")

if (eletkor >= 0 and eletkor <= 6):
    print("Ön gyerek")
elif (eletkor >=7 and eletkor <= 18):
    print("Ön tanuló")
elif (eletkor >= 19 and eletkor <=65):
    print("Ön dolgozó")
else:
    print("Ön nyugdíjas")