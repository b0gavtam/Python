#csomagok importálása
import os
# import keyboard
import time
 
#változók definiálása
 
#a szám amit be kell olvasni
#kezdőértéke None, mivel a while ciklusban ki tudom ezt használni az ismétlések vizsgálatára,
#vagyis a ciklus mindaddig futtatjuk, míg a number változónak nem lesz szám értéke
number: int = None 
    #segéd változó, a beolvasott értéket fogja tárolni
data: str = ""
 
#while ciklus, ami mindaddig fog futni míg a number változó nem kap szám értéket, 
#azaz, az értéke nem None lesz
while(number >= 0 and number < 10):
    #beolvasás a konzolról és a beolvasott értéket eltároljuk a data változóba
    data = input("Kerem a szamot:")
    #megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható-e
    #isdigit() --> bool típusú változót ad vissza
    if(data.isdigit()):
        #ha az isdigit() függvény értéke igaz, akkor számot írt be a felhasználó
        #amit mi BIZTOS át tudunk szám típussá alakítani
        number: int = data
# az isdigit() függvényérték hamis, azaz a felhasználó nem számot írt be,
# így a number változó értéke továbbra us None marad, azaz a felhasználó nem számot írt be
# a ciklust ismételni kell
    else:
        print("\nNem szamot adott meg!")
        #a programot futtató szálat (thread) elaltatjuk 3 másodpercre
        time.sleep(3)
        #letöröljük a képernyőt
        os.system("cls")
       # print("\nA folytatásjoz nymoja meg az ENTER billenyűt")
       #egy végtelen while ciklust írunk, mivel arra fogunk várni, hogy a felhasználó lenyomja a kért billentyűt(ENTER)
        #while (True):
            #figyeljük, hogy a felhasználó lenyomta e az ENTER gombot
                #   if(keyboard.is_pressed('enter')):
                    #      os.system("cls")
                        #kilépünk a belső (végtelen) ciklusból
                        #break
 
#kiírjuk a beolvasott számot                    
print(f"A beolvasott szám {number}")