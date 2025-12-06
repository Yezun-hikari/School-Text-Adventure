import effects
import rooms
import sys


def main():
    effects.clear_screen()
    effects.header('School Adventure', '1')
    effects.header('by Alf, Luisa, Lotte, Mia and Tim', '0')
    print("")

    while True:
        effects.write("Möchtest du das Spiel starten?")
        yn = input("Y/n: ")
        effects.clear_screen()
        
        if yn == "Y":
            rooms.outside()
            sys.exit()

        elif yn == "n":
            effects.write("Okay...")
            effects.write("Vielleicht ja ein andermal :)")
            effects.game_over('School Adventure')
            sys.exit()

        else:
            print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

main()