class derekszogu3szog:
    def __init__(self, a:float, b:float, c:float, m:float):
        super().__init__()

        self.a = a
        self.b = b
        self.c = c
        self.m = m



    def kerulet(self)->float:
        return self.a + self.b + self.c


    def terulet(self)-> float:
        return (self.a*self.b) / 2


    def __str__(self)-> str:
        return f"-a- befogó = {self.a}, \n-b- befogó = {self.b}, \nátfogó = {self.c} \nmagasság = {self.m} \nkerület = {self.kerulet()} \nterület= {self.terulet()}"