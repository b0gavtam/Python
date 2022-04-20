class RAM:
    def __init__(self, gyarto:str, tipus:str, foglalat:str, teljesitmeny:int):
        super().__init__()
        
        self.gyarto = gyarto
        self.tipus = tipus
        self.foglalat = foglalat
        self.teljesitmeny = teljesitmeny
        
        
    def __str__(self)->str:
        return f"Gyártó: {self.gyarto}, \nTípus: {self.tipus}, \nFoglalat: {self.foglalat}, \nTeljesítmény: {self.teljesitmeny} GB"
        