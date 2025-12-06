# Importiert alle notwendigen Funktionen und Module.
from random import *  # Für Zufallszahlen-Generierung.
from effects import * # Modul für visuelle Effekte.
import rooms          # Modul, das die Spiellogik der Räume enthält.
from sys import *     # Für Systemfunktionen wie das Beenden des Spiels.


def door_lock(lockpicks):
    """
    Simuliert ein Minispiel zum Schlossknacken.
    Der Spieler muss eine zufällige Zahl zwischen 1 und 5 erraten.
    Gibt 777 bei Erfolg und 6 bei Misserfolg zurück.
    """
    write("Du hast noch " + str(lockpicks) + " Ditriche übrig.")
    count = 2  # Anzahl der Versuche.
    random_number = randint(1, 5)  # Generiert die zu erratende Zahl.
    
    while count > 0:
        guess = input("Rate: ")
        if guess == "" or not guess.isdigit():
            print("Die Eingabe war ungültig, schreibe eine positive Zahl von 1 bis 5")

        elif int(guess) == random_number:
            write("Hurra!")
            write("Du hast das Schloss erfolgreich geknackt.")
            return 777  # Gibt einen Erfolgscode zurück.
    
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
    
    return 6  # Gibt einen Fehlschlagscode zurück, wenn der Dietrich bricht.


def percent(percentage):
    """
    Eine Funktion, die eine prozentuale Erfolgschance simuliert.
    Gibt 1 bei Erfolg und 0 bei Misserfolg zurück.
    """
    random_val = randint(1, 100)

    if random_val < percentage:  # Überprüft, ob die Zufallszahl im Erfolgsbereich liegt.
        return 1
    
    else:
        return 0
    

def main_door():
    """
    Steuert die Interaktion an der Haupteingangstür.
    Fragt den Spieler, ob er die Eingangshalle betreten möchte.
    """
    while True:
        write("Möchtest du die Eingangshalle betreten?")
        yn = input("Y/n: ")
        clear_screen()

        if yn == "Y":
            write("Du betrittst die Eingangshalle und dich überwältigt ein Gefühl...")
            write("Es fühlt sich finster an, da alles so ruhig und leer ist.")
            write("In der Weite kannst du eine Flasche Rattenspray erkennen.")
            rooms.main_hall()  # Wechselt in die Haupthalle.
            break # Beendet die Schleife nach erfolgreichem Betreten.

        elif yn == "n":
            write("Du hast dich umentschieden...")
            write("Du hast ein unwohles gefühl und kehrst zurrück...")
            game_over('Ende 2')
            sys.exit()
        else:
            print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")


