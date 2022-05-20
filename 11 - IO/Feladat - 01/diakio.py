from statistics import mode
from diak import Diak
from typing import *
import io
import os

class DiakIO:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def read(fileName: str) -> List[Diak]:
        oneLine:str = None
        allLines:List[str]=[]
        
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path,encoding='latin-1', mode="r") as file:
                for line in file:
                    oneLine = line.strip()
                    allLines.append(oneLine)
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")
        
        diakok: List[Diak] = []
        diak: Diak = None
        
        adatok: List[str] = []
        
        nev: str = None
        atlag: float = None

        for line in allLines:
            adatok = line.split('\t')

            nev = adatok[0]
            atlag = float(adatok[1])

            diak = Diak(nev, atlag)
            diakok.append(diak)

        return diakok
    
    @staticmethod
    def write(fileName:str, diakok:List[Diak])-> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding='utf-8', mode="w") as file:
                for diak in diakok:    
                    file.write(f"{diak.nev}\t {diak.atlag}\n")
        except Exception as ex:
            print(f"{ex}")