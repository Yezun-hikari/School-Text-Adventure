# Importiert die notwendigen Module für die Spielfunktionen.
from random import *
from effects import *
import rooms
from sys import *


def door_lock(lockpicks):
    """
    Simuliert das Knacken eines Schlosses.
    Der Spieler muss eine zufällige Zahl erraten.
    Gibt 777 bei Erfolg und 6 bei Misserfolg zurück.
    """
    write("Du hast noch " + str(lockpicks) + " Ditriche übrig.")
    count = 2
    random = randint(1,5)
    
    while count > 0:
        guess = input("Rate: ")
        if guess == "":
            print("Die Eingabe war ungültig, schreibe eine positive Zahl von 1 bis 5")

        elif int(guess) == random:
            write("Hurra!")
            write("Du hast das Schloss erfolgreich geknackt.")
            return 777  # Gibt 777 zurück, wenn das Schloss geknackt wurde.
    
        else:
            if int(guess) > 0:  # Überprüft, ob die Eingabe eine positive Zahl ist.
                if count == 1:
                    write("Leider Falsch, der Dietrich ist gebrochen...")
                    count = count - 1

                else:
                    write("Das war leider Falsch. Versuche es erneut!")
                    count = count - 1

            else:
                print("Die Eingabe war ungültig, schreibe eine positive Zahl von 1 bis 5")
    
    return 6  # Gibt 6 zurück, wenn der Dietrich bricht.


def percent(percentage):
    """
    Eine Funktion, die eine prozentuale Erfolgschance simuliert.
    Gibt 1 bei Erfolg und 0 bei Misserfolg zurück.
    """
    random = randint(1, 100)

    if random < percentage:  # Überprüft, ob die zufällig generierte Zahl im Bereich von 1 bis zum Prozentsatz liegt.
        return 1
    
    else:
        return 0
    

def main_door():
    """
    Logik für die Haupttür, nachdem das Schloss geknackt wurde.
    """
    while True:
        write("Möchtest du die Eingangshalle betreten?")
        yn = input("Y/n: ")
        clear_screen()

        if yn == "Y":
            write("Du betrittst die Eingangshalle und dich überwältigt ein Gefühl...")
            write("Es fühlt sich finster an, da alles so ruhig und leer ist.")
            write("In der Weite kannst du eine Flasche Rattenspray erkennen.")
            rooms.main_hall()

        elif yn == "n":
            write("Du hast dich umentschieden...")
            write("Du hast ein unwohles gefühl und kehrst zurrück...")
            game_over('Ende 2')
            sys.exit()
        else:
            print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")


