# Importiert die notwendigen Module für das Spiel.
import effects  # Modul für visuelle Effekte wie Text-Header und Schreibanimation.
import rooms  # Modul, das die verschiedenen Räume und die Spiellogik enthält.
import sys  # Modul für den Zugriff auf system-spezifische Parameter und Funktionen.
from functions import get_yes_no_input


def main():
    """
    Die Hauptfunktion des Spiels.
    Initialisiert den Bildschirm, zeigt den Titel an und startet die Hauptschleife des Spiels.
    """
    effects.clear_screen()  # Leert den Bildschirm, um eine saubere Anzeige zu gewährleisten.
    effects.header('School Adventure', '1')  # Zeigt den Haupttitel des Spiels an.
    effects.header('by Alf, Louisa, Lotte, Mia and Tim', '0')  # Zeigt die Autoren des Spiels an.
    print("")

    # Hauptschleife, die den Spieler fragt, ob er das Spiel starten möchte.
    while True:
        effects.write("Möchtest du das Spiel starten?")
        yn = get_yes_no_input("Y/n: ")  # Wartet auf die Eingabe des Spielers.
        effects.clear_screen()  # Leert den Bildschirm nach der Eingabe.
        
        # Überprüft die Eingabe des Spielers.
        if yn == "Y":
            rooms.outside()  # Startet das Spiel im Außenbereich.
            sys.exit()  # Beendet das Programm, nachdem das Spiel vorbei ist.

        elif yn == "n":
            effects.write("Okay...")
            effects.write("Vielleicht ja ein andermal :)")
            effects.game_over('School Adventure')  # Zeigt den "Game Over"-Bildschirm an.
            sys.exit()  # Beendet das Programm.

# Startet die Hauptfunktion, wenn das Skript ausgeführt wird.
main()
