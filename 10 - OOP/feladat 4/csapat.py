from szekhely import *
from jatekosok import *
from typing import *

class Csapat:
    def __init__(self, nev:str, jatekosok:List[Jatekosok], szekhely:Szekhely):
        self.nev:str = nev
        self.jatekosok: List[Jatekosok] = jatekosok
        self.szekhely:Szekhely = szekhely

    def __str__(self)->str:
        valtozo: str = f"Csapatnév:{self.nev}\n"
        for jatekosok in self.jatekosok:
            valtozo += f"Játékosok: {str(jatekosok)}\n"
        
        return valtozo 