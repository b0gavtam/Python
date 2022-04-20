from alaplap import *
from cpu import *
from gpu import *
from ram import *
from hdd import *

class PC:
    def __init__(self, alaplap:Alaplap, cpu:CPU, ram:RAM, hdd:HDD, gpu:GPU):
        super().__init__()        
        self.alaplap: Alaplap = alaplap
        self.cpu: CPU = cpu
        self.ram: RAM = ram
        self.hdd: HDD = hdd
        self.gpu: GPU = gpu 

    def __str__(self)->str:
        return f"Alaplap: {self.alaplap}, \nCPU:{self.cpu}, \nRAM: {self.ram}, \nHDD = {self.hdd}, \nGPU: {self.gpu}"


        
        