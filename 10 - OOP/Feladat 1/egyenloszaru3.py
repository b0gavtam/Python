class egyenloszaru3szog:
    def __init__(self, a:float, b: float, m:float):
        super().__init__()

        self.a = a
        self.b = b
        self.m = m



    def kerulet(self)->float:
        return (2*self.b) + self.a


    def terulet(self)-> float:
        return (self.a*self.m) / 2


    def __str__(self)-> str:
        return f"alap = {self.a}, \nszárak = {self.b}, \nmagasság = {self.m} \nkerület = {self.kerulet()} \nterület= {self.terulet()}"