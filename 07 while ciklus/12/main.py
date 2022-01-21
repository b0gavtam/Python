data:str=""
penz:float=0
honapokSzama:int=0

while (penz < 10000 or penz > 50000):
    data=input(("10,000 és 50,000 között adon meg pénzmennyiséget: "))
    if(data.isnumeric()):
        penz=float(data)
        if (penz <10000 or penz>50000):
            print("10,000 és 50,000 között adja meg pénzét! ")

while(penz<100000):
    honapokSzama+=1
    penz=penz*1.02

print(f"{honapokSzama} hónapig kell hogy kamatozzon a pénz 2%os kamattal, hogy 100,000 legyen")