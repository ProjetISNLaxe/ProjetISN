
from snake import *

def quetes(fenetre):
    activefich=open("quetes\\active", "r")
    active=activefich.read()
    activefich.close()
    if active=="marie":
        marie(fenetre)
    if active=="patrick":
        patrick(fenetre)
def marie(fenetre):
    activefich = open("quetes\\pnjrencontre", "r")
    active = activefich.read()
    activefich.close()
    dragonfi=open("quetes\\marie\\dragon", "r")
    dragon=dragonfi.read()
    dragonfi.close()
    litransifi = open("quetes\\visitelieu", "r")
    lieu=litransifi.read()
    litransifi.close()

    if active=="dragon" and dragon=="0":
        toprintfi=open("quetes\\marie\\toprint", "w")
        toprintfi.write("Effectuez un score de 10 au snake")
        toprintfi.close()
        pygame.image.save(fenetre, "inventory/fond.jpg")
        score= snake(fenetre)
        if score>=10:
            toprintfi = open("quetes\\marie\\toprint", "w")
            toprintfi.write("Allez voir Patrick")
            toprintfi.close()
            dragonfi1 = open("quetes\\marie\\dragon", "w")
            dragonfi1.write("1")
            dragonfi1.close()

    if active == "patrick" and dragon=="1":
        activefich = open("quetes\\active", "w")
        activefich.write("")
        activefich.close()
        dragonfi = open("quetes\\marie\\dragon", "w")
        dragonfi.write("0")
        dragonfi.close()
        toprintfi = open("quetes\\marie\\toprint","w")
        toprintfi.write("Allez voir le dragon")
        toprintfi.close()
        todo=open("quetes\\liste", "w")
        todo.write("patrick")
        todo.close()
def patrick():
    activefich = open("quetes\\pnjrencontre", "r")
    active = activefich.read()
    activefich.close()
    litransifi = open("quetes\\visitelieu", "r")
    lieu=litransifi.read()
    litransifi.close()

    if active == "marie":
        activefich = open("quetes\\active", "w")
        activefich.write("")
        activefich.close()
        toprintfi = open("quetes\\patrick\\toprint","w")
        toprintfi.write("Allez voir Marie")
        toprintfi.close()



