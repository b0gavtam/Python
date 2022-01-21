from matematika_fuggvenyek import *
from inputLib import *

osszeg: float = None
kulonbseg: float = None
szorzat: float = None
hanyados: float = None

szam1: float = None
szam2: float = None

szam1=tizedesSzamBeolvasas("Kérem az első számot: ")
szam2=tizedesSzamBeolvasas("Kérem a második számot: ")

osszeg=osszeadas(szam1, szam2)
kulonbseg=kivonas(szam1, szam2)
szorzat=szorzas(szam1, szam2)
hanyados=osztas(szam1,szam2)

print(f"\nA 2 szám összege: {osszeg}\nkülómbségük: {kulonbseg},\nszorzatuk: {szorzat},\nhányadosuk:{hanyados}")