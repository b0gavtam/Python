import time
import os

rendeles:int=0

while(rendeles<1 or rendeles >5):
    rendelesInput=input("Nyomja meg a menü előtti számot a kívánt üdítőért:\n1 - Ice Tea\n2 - Limunádé\n3 - Epres jégkása\n4 - Almalé\n 5 - szénsavmentes víz")
    if(rendelesInput.replace("-", "").isnumeric()):
        rendeles=int(rendelesInput)
        if (rendeles < 1 or rendeles>5):
            print("Csak a megadott opciókból lehet választani")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

if(rendeles==1):
    print("Élvezze a kóláját")
elif(rendeles==2):
    print("Élvezze a limonádéját")
elif(rendeles==3):
    print("Élvezze a fantáját")
else:
    print("Élvezze a spriteját")