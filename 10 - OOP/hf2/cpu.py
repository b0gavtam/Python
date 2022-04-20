class CPU:
    def __init__(self, gyarto:str, tipus:str,  orajel:float, mag:int, memoria:int):
        super().__init__()
        
        self.gyarto = gyarto
        self.tipus = tipus
        self.orajel = orajel
        self.mag = mag
        self.memoria = memoria
    
    def __str__(self)->str:
        return f"Gyártó: {self.gyarto}, \nTípus:{self.tipus}, \nÓrajel: {self.orajel} GHz, \nMag: {self.mag}, \nMemória: {self.memoria} GB"