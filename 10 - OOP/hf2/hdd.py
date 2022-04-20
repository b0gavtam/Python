class HDD:
    def __init__(self, gyarto:str, tipus:str, tarhely:str, rpm:int):
        super().__init__()
        
        self.gyarto = gyarto
        self.tipus = tipus
        self.tarhely = tarhely
        self.rpm = rpm
        
        
    def __str__(self)->str:
            return f"Gyártó: {self.gyarto}, \nTípus: {self.tipus}, \nTárhely: {self.tarhely} TB, \nRPM: {self.rpm}"    