class Teglalap:

    def __init__(self, hossz: float, szelesseg:float)-> None:
        super().__init__()

        #adattagok definiálása
        self.hossz = hossz
        self.szelesseg = szelesseg


    def terulet(self)-> float:
        return self.hossz*self.szelesseg

    def kerulet(self)-> float:
        return 2 * (self.hossz+self.szelesseg)   