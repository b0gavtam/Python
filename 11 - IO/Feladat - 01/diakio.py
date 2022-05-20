from ast import List
import io
from diak import *
from typing import *
class DiakIO:
    def __init__(self) -> None:
        super().__init__()
        
    @staticmethod
    def read(fileName:str) -> List[Diak]:
        oneline:str = None
        allines:List[str] = []
        try:
            with open("./adatok.txt", encoding='utf-8', mode="r") as file:
                for line in file:
                    oneLine = line.strip()
                    allines.append(oneLine)
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")
            
        diakok:List[Diak] = []
        diak:Diak = None
        adatok:List[str] = []
        nev:str = None
        atlag:float = None
            
        for line in allines:
            adatok = line.split('\t')
              
              
            nev:adatok[0]
            atlag:float(adatok[1])
              
            diak = Diak(nev, atlag)
            diakok.append(diak)
            
        return diakok