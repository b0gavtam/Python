class Tanulo:
    def __init__(self, vezeteknev:str, keresztnev:str, szulido:str):
        super().__init__()
        self.vezeteknev:str = vezeteknev
        self.keresztnev:str = keresztnev
        self.szulido:str = szulido


    def __str__(self):
        return f"Vezetéknév: {self.vezeteknev}, Keresztnév: {self.keresztnev}, Szül. idő: {self.szulido}"
        
    