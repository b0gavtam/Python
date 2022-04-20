class Tulaj:
    def __init__(self, nev:str, szulido:str,szulhely:str, nem:str) -> None:
        super().__init__()
        
        self.nev : str = nev
        self.szulido: str = szulido
        self.szulhely:str = szulhely
        self.nem: str = nem
        
        
        
    def __str__(self)->str:
        return f"{self.nev} \nSzületési idő = {self.szulido} \nSzületési hely = {self.szulhely} \nNem = {self.nem}"