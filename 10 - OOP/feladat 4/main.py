from csapat import *

szekhelye:Szekhely= Szekhely("Szeged", 6722, "Csongrád", "Gutenberg", 11)

ichi:Jatekosok = Jatekosok("Kala","Pál", 1, "fogadó")
ni:Jatekosok = Jatekosok("Beterp","Eszter",21,"fogadó")
san:Jatekosok = Jatekosok("Kihor","Dani",5,"center")
yon:Jatekosok = Jatekosok("Gec","Imre",10,"négyesütő")
go:Jatekosok = Jatekosok("Szippan","Csáki",8,"szélesütő")
roku:Jatekosok = Jatekosok("Tökeo","Lajos",9,"libero")

csapat:Csapat = Csapat("SZRSE", [ichi,ni,san,yon,go,roku], szekhelye)
print(csapat)
