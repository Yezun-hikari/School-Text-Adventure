# Importiert die notwendigen Module für die Spielfunktionen.
from random import *
from effects import *
import rooms
from sys import *


def get_integer_input(prompt, min_val=None, max_val=None, range_error_message="Ungültige Eingabe."):
    """
    Nimmt eine Eingabe vom Benutzer entgegen und stellt sicher, dass es sich um eine gültige Ganzzahl in einem bestimmten Bereich handelt.
    """
    while True:
        try:
            value = int(input(prompt))
            if (min_val is not None and value < min_val) or \
               (max_val is not None and value > max_val):
                print(range_error_message)
            else:
                return value
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")

def get_yes_no_input(prompt):
    """
    Nimmt eine 'Y/n'-Eingabe vom Benutzer entgegen und stellt sicher, dass sie gültig ist.
    """
    while True:
        choice = input(prompt)
        if choice in ["Y", "n"]:
            return choice
        else:
            print("Ungültige Eingabe. Bitte geben Sie 'Y' oder 'n' ein.")


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
        guess = get_integer_input("Rate: ", min_val=1, max_val=5, range_error_message="Die Eingabe war ungültig, schreibe eine positive Zahl von 1 bis 5")
        if guess == random:
            write("Hurra!")
            write("Du hast das Schloss erfolgreich geknackt.")
            return 777  # Gibt 777 zurück, wenn das Schloss geknackt wurde.
    
        else:
            count -= 1
            if count > 0:
                write("Das war leider Falsch. Versuche es erneut!")
            else:
                write("Leider Falsch, der Dietrich ist gebrochen...")
    
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
        yn = get_yes_no_input("Y/n: ")
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
