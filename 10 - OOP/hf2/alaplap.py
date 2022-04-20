class Alaplap:
    def __init__(self, gyarto:str, tipus:str):
        super().__init__()
        
        self.gyarto = gyarto
        self.tipus = tipus
        
        
    def __str__(self)->str:
        return f" Gyártó: {self.gyarto}, \nTípus: {self.tipus}"