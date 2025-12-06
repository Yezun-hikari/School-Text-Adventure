# Importiert die notwendigen Module für das Spiel.
import effects  # Modul für visuelle Effekte wie Text-Header und Schreibanimationen.
import rooms    # Modul, das die verschiedenen Räume und deren Logik enthält.
import sys      # Modul für den Zugriff auf Systemfunktionen, hier zum Beenden des Spiels.


def main():
    """
    Die Hauptfunktion des Spiels.
    Initialisiert den Bildschirm, zeigt den Titel an und startet die Hauptschleife des Spiels.
    """
    effects.clear_screen()  # Leert den Bildschirm, um eine saubere Anzeige zu gewährleisten.
    effects.header('School Adventure', '1')  # Zeigt den Haupttitel des Spiels an.
    effects.header('by Alf, Luisa, Lotte, Mia and Tim', '0')  # Zeigt die Autoren an.
    print("")  # Fügt eine Leerzeile für bessere Lesbarkeit hinzu.

    # Startet eine Endlosschleife, um den Spieler zu fragen, ob er das Spiel starten möchte.
    while True:
        effects.write("Möchtest du das Spiel starten?")
        yn = input("Y/n: ")  # Wartet auf die Eingabe des Spielers.
        effects.clear_screen()  # Leert den Bildschirm nach der Eingabe.
        
        # Überprüft die Eingabe des Spielers.
        if yn == "Y":
            rooms.outside()  # Startet das Spiel im Außenbereich.
            sys.exit()  # Beendet das Programm, wenn das Spiel vorbei ist.

        elif yn == "n":
            effects.write("Okay...")
            effects.write("Vielleicht ja ein andermal :)")
            effects.game_over('School Adventure')  # Zeigt den "Game Over"-Bildschirm an.
            sys.exit()  # Beendet das Programm.

        else:
            # Informiert den Spieler über eine ungültige Eingabe.
            print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

# Ruft die Hauptfunktion auf, um das Spiel zu starten.
main()