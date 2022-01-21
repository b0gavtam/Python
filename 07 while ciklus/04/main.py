import os
import time
 
number: int = None
data: str = ""
 
while(number==None or number > 10 or number < 0):
    data = input("Kerek egy 1 és 9 közötti számot:")
    if(data.replace("-", "").isnumeric()):
        number=int(data)    
        if((int(number) > 10 or int(number) < 0)):
            print("\nNem 1 és 9 közötti számot adott meg") 
            time.sleep(3)
            os.system("cls")  
    else:
        print("\nNem számot adott meg!")
        time.sleep(3)
        os.system("cls")

print(f"A beolvasott szám: {number}")