from csapat import *
from jatekosokfajl import *
from szekhely import *

szekhelye:Szekhely= Szekhely("Szeged", 6722, "Csongrád", "Gutenberg", 11)

egy:Jatekosok = Jatekosok("Kala","Pál", 1, "fogadó", 22)
ketto:Jatekosok = Jatekosok("Beterp","Eszter",21,"fogadó", 23)
harom:Jatekosok = Jatekosok("Kihor","Dani",5,"center", 52)
negy:Jatekosok = Jatekosok("Vas","Imre",10,"négyesütő", 41)
ot:Jatekosok = Jatekosok("Szippan","Csáki",8,"szélesütő", 65)
hat:Jatekosok = Jatekosok("Tökeo","Lajos",9,"libero",55)

jatekoslista:List[Jatekosok] = []
jatekoslista.append(egy)
jatekoslista.append(ketto)
jatekoslista.append(harom)
jatekoslista.append(negy)
jatekoslista.append(ot)
jatekoslista.append(hat)

csapat:Csapat = Csapat("SZRSE", [egy,ketto,harom,negy,ot,hat], szekhelye)
print(csapat)


print("A legtöbb pontszámmal rendelkező játékos: \n")
print(csapat.legjobbjatekos())



print("Mezszámszerinti rendezés: \n ")
print(novekvosorrend)
