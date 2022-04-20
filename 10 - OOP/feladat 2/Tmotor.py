from tulajdonos import *

class Tmotor:
    def __init__(self, gyarto:str, tipus:str, kivitel:str, teljesitmeny:int, suly:int, hengerurtartalom:int,tulajdonos: Tulaj):
        super().__init__()
        
        self.gyarto: str = gyarto
        self.tipus: str = tipus
        self.kivitel: str = kivitel
        self.teljesitmeny: str = teljesitmeny
        self.suly: int = suly
        self.hengerurtartalom:int = hengerurtartalom
        self.tulajdonos : Tulaj = tulajdonos
        
        
    def __str__(self)->str:
        return f"gyártó = {self.gyarto} \ntípus = {self.tipus} \nkivitel = {self.kivitel} \nteljesítmény = {self.teljesitmeny}LE \nsúly = {self.suly}kg \nhengerurtartalom = {self.hengerurtartalom}cm2 \nTulajdonos = {self.tulajdonos}"