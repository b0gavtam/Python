#pip3 install keyboard

#/csomagok importálása
#import os
#import keyboard
#import time

#/változók definiálálsa

#/a szám amit be kell olvasni
#/kezdőértéke a None, mivel a while ciklusban tufom ezt használni az ismétlések vizsgálatára,
#/vagyis a ciklust mindaddig futtatjuk, ameddig a number változónak nem lesz szám értéke

number: float = None #/segédváltozó, a beolvasott értéket fogja tárolni


data: str = ""


while(number == None): #/while ciklus ami addig fog futni, amíg a number változó nem kap szám értéket, azaz az értéke None lesz
        
        #/beolvasás a konzolról és a beolvasott értéket eltároljuk a data változóba
        data = input ("Kérem a számot")
        
        #/megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható-e
        #/mindegy, hogy a szám int vagy float típusú
        #/isdigit()--> bool változót ad vissza
        if(data.isdigit()):
            #/ha az isdigit() függvény értéke igaz, akkor számot írt be a felhasználó
            #/amit BIZTOS át tudunk szám típussá alakítani
            number = float(data)
        #/ha az isdigit() értéke hamis, akkor a felhasználó nem számot írt be
        #/így a number változó értéke None marad, azaz a felhasználó nem számot írt be
        #/a ciklust ismételni kell
        
        else:
            print("\nNem számot adott meg!") 
            time.sleep(3)   #/a programot futtató szálat (thread) elaltatjuk 3 másodpercre
            os.system("cls") #/letöröljük a képernyőt
            #print("\nA folytatáshoz nyomjon ENTER gombot") /#egy végtelen WHILE ciklust íruk, mivel arra fogunk várni, hogy a felhasználó lenyomja a kért billentyűt (ENTER)
            #while(True):       /#figyeljük, hogy a felhasználó lenyomta-e az ENTER gombot
                #if(keyboard.is_pressed('enter')):
                    #os.system("cls")          / #letöröljük a képernyőt
                      #break
print(f"A beolvasott szám {number}")