# Importiert die notwendigen Module für visuelle Effekte.
import sys
import time
import pyfiglet


def write(text):
    """
    Simuliert einen Schreibmaschineneffekt für den angegebenen Text.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def header(text, size):
    """
    Zeigt einen ASCII-Art-Header mit dem angegebenen Text und der angegebenen Größe an.
    """
    if size == '0':
        sys.stdout.write(pyfiglet.Figlet(font='mini').renderText(text))

    if size == '1':
        sys.stdout.write(pyfiglet.Figlet(font='small').renderText(text))

    if size == '2':
        sys.stdout.write(pyfiglet.Figlet(font='slant').renderText(text))


def clear_screen():
    """
    Leert den Bildschirm, indem 50 leere Zeilen gedruckt werden.
    """
    count = 50
    while count > 0:
        print()
        count = count - 1


def game_over(ending):
    """
    Zeigt den "Game Over"-Bildschirm mit dem angegebenen Ende und den Credits an.
    """
    clear_screen()
    header(ending, '1')
    time.sleep(1)
    print("Game by: Alf, Louisa, Lotte, Mia and Tim")
    time.sleep(1)
    repeat =3
    while repeat > 0:
        time.sleep(1)
        print()
        repeat = repeat - 1
    header('Credits', '0')
    time.sleep(1)
    print()
    time.sleep(1)
    print("Idee: Mia")
    time.sleep(1)
    print()
    time.sleep(1)
    print("Flowchart: Louisa, Lotte, Mia und Tim")
    time.sleep(1)
    print()
    time.sleep(1)
    print("Code: Tim, Alf")

    repeat =20
    while repeat > 0:
        time.sleep(0.5)
        print()
        repeat = repeat - 1

