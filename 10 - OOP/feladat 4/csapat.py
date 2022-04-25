from szekhely import *
from jatekosokfajl import *
from typing import *

class Csapat:
    def __init__(self, nev:str, jatekosok:List[Jatekosok], szekhely:Szekhely):
        super().__init__()
        self.nev:str = nev
        self.jatekosok: List[Jatekosok] = jatekosok
        self.szekhely:Szekhely = szekhely

    def __str__(self)->str:
        valtozo: str = f"Csapatnév:{self.nev}\n"
        for jatekosok in self.jatekosok:
            valtozo += f"Játékosok: {str(self.jatekosok)}\n"
        
        return valtozo
        



    def legjobbjatekos(self) -> Jatekosok:
        max: Jatekosok = self.jatekosok[0]

        for i in range(1, len(self.jatekosok)):
            if(self.jatekosok[i].pontszam > max.pontszam):
                max = self.jatekosok[i]


        return max


    def mezrendezes(self)->List[Jatekosok]:
        valtozo:List[Jatekosok] = self.jatekosok.copy()
        for i in range(0,len(valtozo),1):
            for j in range(i, len(valtozo), 1):
                if(valtozo[i].mezszam > eredmeny[j].mezszam):
                    temp = eredmeny[i]
                    valtozo[i] = valtozo[j]
                    valtozo[j] = temp
        return valtozo



