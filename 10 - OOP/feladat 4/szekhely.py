class Szekhely:
    def __init__(self, telepules:str, iranyitoszam:int, megye:str, kozterulet:str, kozteruletszam:int):
        self.telepules: str = telepules
        self.iranyitoszam:int = iranyitoszam
        self.megye: str = megye
        self.kozterulet: str = kozterulet
        self.kozteruletszam:int = kozteruletszam


    def __str__(self):
        return f"Település:{self.telepules},\nIrányítószám:{self.iranyitoszam},\nMegye:{self.megye},\nKözterület:{self.kozterulet},\nKözterületszám:{self.kozteruletszam}"    