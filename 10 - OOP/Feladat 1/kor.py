import math


class Kor:
    def __init__(self, sugar:float):
        super().__init__()

        self.sugar = sugar



    def kerulet(self)->float:
        return (2*self.sugar) * math.pi


    def terulet(self)-> float:
        return (self.sugar*self.sugar)* math.pi 


    def __str__(self)-> str:
        return f"sugár = {self.sugar}, \nkerület = {self.kerulet()} \nterület= {self.terulet()}"