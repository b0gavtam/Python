class GPU:
    def __init__(self, gyarto:str, tipus:str, memoria:int, orajel:float):
        super().__init__()
        
        self.gyarto = gyarto
        self.tipus = tipus
        self.memoria = memoria
        self.orajel = orajel
        
    def __str__(self)->str:
        return f"Gyártó: {self.gyarto}, \nTípus: {self.tipus} \nMemória: {self.memoria} GB, \nAlapórajel: {self.orajel} GHz"    