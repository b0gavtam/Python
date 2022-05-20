from random import random
from typing import *
import random

class Jatekos:
    def __init__(self, nev:str, tippek:Set[int]):
        super().__init__()
        
        self.nev:str = nev
        self.tippek:Set[int] = tippek
        
        
        
    def __str__(self) -> str:
        return f"A játékos neve: {self.nev} \n A játékos tippjei: {self.tippek}"
    
    
    def halmazmetszet(self, nyeroszamok:Set[int])-> Set[int]:
        return self.tippek.intersection(nyeroszamok)
          