from jatekos import *


def randomSzamok() -> Set[int]:
    eredmeny:Set[int] = {random.randint(1,99)}
    while(len(eredmeny) < 5):
        szam = random.randint(1,99)
        eredmeny.add(szam)
    
    return eredmeny  





kihuzottszamok: Set[int] = randomSzamok()
print(kihuzottszamok)

tippek: Set[int] = randomSzamok()



jatekos1: Jatekos = Jatekos("Amo Gus", tippek)
print(jatekos1)


eltalaltszamok:Set[int] = jatekos1.halmazmetszet(kihuzottszamok)
if(len(eltalaltszamok) == 0):
    print("nincs megegyező szám")
else:
    print(f"A megegyező számok: {eltalaltszamok}")