import random

class Szuperhos:
    def __init__(self, nev:str)-> None:
        super().__init__()
        
        self.nev:str = nev
        self.hp:int = random.randint(60,90)
        self.ero:int = random.randint(50,100)


    def __str__(self):
        return f"ném:{self.nev},\n póver:{self.ero}\n hápé:{self.hp} \n" 


    def tamad(self,ellenseg:"Szuperhos")-> bool:   #saját programban saját objektumra idézőjellel lehet hivatkozni (rósz pYthno)
         return self.ero >= ellenseg.hp
            
