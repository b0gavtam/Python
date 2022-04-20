from tanulo import *
from typing import *

class Csoport:
    def __init__(self, csoportnev:str, tanulok:List[Tanulo]):
        super().__init__()
        self.csoportnev:str=csoportnev
        self.tanulok:List[Tanulo]=tanulok

    def __str__(self)->str:
        return f"Csoport neve: {self.csoportnev}, tagjai : "
    
    def tagokkiratasa(self):
        for tag in self.tanulok:
            print(tag)