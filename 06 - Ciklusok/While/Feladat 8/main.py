szam:int = 0
data:str =""

while(szam > 4 or szam <= 0):
    data = input("Adjon meg egy számot egytől négyig: 1-Hell, 2-Tea, 3-Fanta, 4-Pepsi:")
    if(data.replace("-", " ").isnumeric()):
        szam = int(data)
    if(szam > 4 or szam <=0):
        print("Rossz számot, vagy nem számot adott meg, nem kap üdítőt.")

if(szam == 1):
    print("Itt a Hell-je")
elif(szam == 2):
    print("Itt az ön Teája")
elif(szam == 3):
    print("Itt az ön Fantája")
elif(szam == 4):
    print("Itt az ön Pepsije")