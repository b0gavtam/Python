from turtle import clear
from diak import *
from typing import * 
from diakio import *

class Osztaly:
    
    @staticmethod
    def atlag(diakok:List[Diak]) -> float:
        atlag:float = 0
        osszeg:float = 0
        
        for diak in diakok:
            osszeg+= diak.atlag
        
        atlag = osszeg / len(diakok)
        
        
        return atlag
    
    @staticmethod
    def legjobbak(diakok:List[Diak]) -> List[Diak]:
        jodiakok:List[Diak] = [diakok[0]]
        legjobb:Diak = diakok[0]
        
        for i in range(1, len(diakok), 1):
            if(diakok[i].atlag > jodiakok[0].atlag):
                jodiakok.append(diakok[i])
                legjobb = diakok[i]
            elif(diakok[i].atlag == jodiakok[0].atlag):
                jodiakok.clear()
                jodiakok.append(diakok[i])
            
        
        return jodiakok

    @staticmethod
    def atlagfelettiek(diakok:List[Diak], atlag: float)-> None:
        atlagfelettiek:List[Diak] = []

        for diak in diakok:
            if(diak.atlag > atlag):
                atlagfelettiek.append(diak)



        DiakIO.write("atlagfelettiek.txt", atlagfelettiek)    




    def vanekitunotanulo(diakok:List[Diak])-> bool:
        van:bool= False
        for diak in diakok:
            if(diak.atlag ==5.00):
                van = True
                break
        
        
        return van
    
    
    """@staticmethod
    def besorolas(diakok: List[Diak], elegtelen: List[Diak], elegseges: List[Diak], jo: List[Diak], jeles: List[Diak], kituno: List[Diak]) -> None:

        
        for diak in diakok:
            if(0.00<=diak.atlag<=1.99):
                elegtelen.append(diak)
            elif(2.00<=diak.atlag<=2.99):
                elegseges.append(diak)
            elif(3.00<=diak.atlag<=3.99):
                jo.append(diak)
            elif(4.00<=diak.atlag<=4.99):
                jeles.append(diak)
            elif(diak.atlag==5):
                kituno.append(diak)"""
    """@staticmethod
    def besorolas(diakok: List[Diak]) -> Dict[str,int]:
        eredmeny:Dict[str, int] = {
            elegtelen:int = 0
            elegseges:int = 0
            jo:int = 0
            jeles:int = 0
            kituno:int = 0
        }
        for diak in diakok:
            if(0.00<=diak.atlag<=1.99):
                eredmeny[elegtelen]+= 1
            elif(2.00<=diak.atlag<=2.99):
                eredmeny[elegseges]+=1
            elif(3.00<=diak.atlag<=3.99):
                eredmeny[jo]+=1
            elif(4.00<=diak.atlag<=4.99):
                eredmeny[jeles]+=1
            elif(diak.atlag==5):
                eredmeny[kituno]+=1"""
    @staticmethod
    def besorolas(diakok:List[Diak])-> Dict[str, int]:

        diakAtlagok:Dict[str, int] = {}

        hatarertekek:Dict[str,int] = {
            "elégtelen" : 1.99,
            "elégséges" : 2.99,
            "jó" : 3.99,
            "jeles" : 4.99,
            "kitűnő" : 5.00
        }

        for (key,value) in hatarertekek.items():
            darab:int = 0

            for diak in diakok:
                if(diak.atlag < value):
                    darab+=1

            diakAtlagok[key] = darab
        
        return diakAtlagok
                



