from typing import List
from csoport import *

tanulo1: Tanulo = Tanulo("Hétfő", "Henrik", "2005.03.21.")
tanulo2: Tanulo = Tanulo("Kedd", "Krisztián", "2004.07.14.")
tanulo3: Tanulo = Tanulo("Szerda", "Szilárd", "2006.05.07.")

tanulok:List[Tanulo] = [tanulo1, tanulo2, tanulo3]
csoport:Csoport = Csoport("10.B haladó", tanulok)
print(csoport)
