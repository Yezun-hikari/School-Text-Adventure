# Importiert die notwendigen Module für das Spiel.
import functions
import effects
import time
import sys

# Definition der Inventare für die verschiedenen Räume und den Spieler.
server_room_inv = ["Netzwerkkabel", "Hammer"]
teacher_inv = ["Gas", "Regal", "Schreibtisch"]
main_hall_inv = ["Rattenspray", "Dietriche", "Verschimmelter Käse"]
basement_inv = ["Gasmaske", "Ratten", "Schaumstoff-Schwert"]
player_inv = []


def room_intro(room_id):
    """
    Zeigt eine spezifische Einleitungsnachricht für einen Raum an,
    abhängig von bestimmten Bedingungen (z.B. ob Gas im Raum ist).
    """
    if room_id == 1:
        if "Gas" in teacher_inv:
            effects.write("Sobald du das Lehrerzimmer betrittst sticht dir ein intensiver Kaffegeruch in die Nase.")
            effects.write("Ohne eine Gasmaske wirst du hier Schnell ersticken...")
            print()
        effects.write("Was möchtest du tun?")

    if room_id == 2:
        if "Ratten" in basement_inv:
            effects.write("Als du den Keller betrittst, hörst du sofort das nagen von Ratten.")
            effects.write("Ein Rattenspray währe eventuell gut...")
            print()
        effects.write("Was möchtest du tun?")


def teacher():
    """
    Definiert die Logik für das Lehrerzimmer.
    Der Spieler kann nach Items suchen, Items verwenden oder in die Haupthalle zurückkehren.
    """
    room_intro(1)

    while True:
        effects.write("1. Nach Items im aktuellen Raum schauen, 2. Item verwenden, 3. Zurück in die Haupthalle")
        yn = input("1/2/3: ")
        effects.clear_screen()

        if yn == "1":
            # Game Over, wenn der Spieler ohne Gasmaske nach Items sucht.
            if "Gas" in teacher_inv:
                effects.write("Du athmest zu viel vom Kaffegeruch ein und fällst zu Boden!")
                time.sleep(2)
                effects.game_over('Ende 5')
                sys.exit()
            else:
                # Logik zur Suche nach Items im Raum.
                while True:
                    effects.write("Du schaust dich im Raum um und siehst folgende Orte, an denen sich Items befinden könnten:")
                    pos = 1
                    for item in teacher_inv:
                        effects.write(str(pos) + ". " + item)
                        pos = pos + 1
                    print()
                    effects.write(str(pos) + ". Zurrück")
                    effects.write("Möchtest du an einem dieser Orte nachschauen?")
                    yn = input("Y/n: ")

                    if yn == "Y":
                        effects.write("An welchem Ort willst du suchen?")
                        item_choice = input("Nummer des Ortes: ")
                        effects.clear_screen()

                        if not item_choice.isdigit():
                            effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Orte.")
                        elif int(item_choice) == len(teacher_inv) + 1:
                            effects.write("Kein Ort wird durchsucht.")
                            break
                        elif 0 < int(item_choice) <= len(teacher_inv):
                            item_choice_idx = int(item_choice) - 1
                            item_searched = teacher_inv[item_choice_idx]

                            if item_searched in ["Regal", "Schreibtisch"]:
                                if functions.percent(50) == 1:
                                    effects.write(f"Du hast die Klassenarbeiten im {item_searched} gefunden!")
                                    effects.write("Du erzählst allen von deinem Erfolg und wirst als Held gefeiert!")
                                    effects.game_over('Gewonnen!')
                                    sys.exit()
                                else:
                                    effects.write(f"Das {item_searched} ist leer...")
                                    time.sleep(2)
                                    effects.write("ES QUITSCHT!")
                                    if functions.percent(75) == 0:
                                        effects.write("Der Hausmeister hat das Quietschen gehört und die Polizei gerufen :/")
                                        time.sleep(2)
                                        effects.game_over('Ende 6')
                                        sys.exit()
                                    else:
                                        effects.write("Zum Glück hat der Hausmeister nichts gehört.")
                        else:
                            effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Orte.")
                    elif yn == "n":
                        effects.clear_screen()
                        effects.write("Es wird an keinem Ort gesucht.")
                        break
                    else:
                        print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

        elif yn == "2":
            # Logik zur Verwendung von Items aus dem Spieler-Inventar.
            effects.write("Welches Item soll verwendet werden?")
            pos = 1
            for item in player_inv:
                effects.write(f"{pos}. {item}" + (" (Kann verwendet werden!)" if item == "Gasmaske" else ""))
                pos += 1
            print()
            effects.write(f"{pos}. Zurrück")

            item_use = input("Nummer des Items: ")
            effects.clear_screen()

            if item_use.isdigit() and 0 < int(item_use) <= len(player_inv):
                item_used = player_inv[int(item_use) - 1]
                if item_used == "Gasmaske":
                    effects.write("Gasmaske anziehen, um dem Kaffegeruch entgegen zu stehen?")
                    if input("Y/n: ") == "Y":
                        effects.write("Du ziehst dir so schnell wie möglich die Gasmaske an...")
                        effects.write("Du holst tief Luft und kannst dich wieder frei Bewegen!")
                        teacher_inv.remove("Gas")
                        player_inv.remove("Gasmaske")
                        time.sleep(2)
                else:
                    effects.write(f"Das Item {item_used} kann hier nicht verwendet werden.")
            elif item_use.isdigit() and int(item_use) == len(player_inv) + 1:
                effects.write("Kein Item wird verwendet.")
            else:
                effects.write("Die Eingabe war ungültig.")

        elif yn == "3":
            effects.write("Du kehrst in die Eingangshalle zurrück...")
            main_hall()
            break

        else:
            print("Die Eingabe war ungültig, schreibe 1, 2 oder 3.")


def server_room():
    """
    Definiert die Logik für den Serverraum.
    Der Spieler kann Items aufnehmen, den Hammer verwenden oder zurückkehren.
    """
    effects.write("Was möchtest du tun?")
    while True:
        effects.write("1. Items im aktuellen Raum anschauen, 2. Item verwenden, 3. Zurück in die Haupthalle")
        yn = input("1/2/3: ")
        effects.clear_screen()

        if yn == "1":
             # Logik zum Aufnehmen von Items.
            while True:
                effects.write("Du schaust dich im Raum um und findest folgende Items:")
                pos = 1
                for item in server_room_inv:
                    effects.write(f"{pos}. {item}")
                    pos += 1
                print()
                effects.write(f"{pos}. Zurrück")
                if not server_room_inv:
                    effects.write("Es sind keine weiteren Items im Raum.")
                    break

                yn_item = input("Möchtest du eines der Items aufnehmen? (Y/n): ")
                if yn_item == "Y":
                    item_choice = input("Nummer des Items: ")
                    if item_choice.isdigit() and 0 < int(item_choice) <= len(server_room_inv):
                        item_taken = server_room_inv.pop(int(item_choice) - 1)
                        player_inv.append(item_taken)
                        effects.write(f"Du nimmst das Item: {item_taken}")
                    else:
                        effects.write("Ungültige Auswahl.")
                else:
                    break

        elif yn == "2":
            # Logik zur Verwendung des Hammers.
            effects.write("Welches Item soll verwendet werden?")
            pos = 1
            for item in player_inv:
                effects.write(f"{pos}. {item}" + (" (Kann verwendet werden!)" if item == "Hammer" else ""))
                pos += 1
            print()
            effects.write(f"{pos}. Zurrück")

            item_use = input("Nummer des Items: ")
            if item_use.isdigit() and 0 < int(item_use) <= len(player_inv):
                if player_inv[int(item_use) - 1] == "Hammer":
                    if input("Hammer verwenden um den Server zu zerstören? (Y/n): ") == "Y":
                        effects.write("Du Zerstörst den Schulserver mit einem Hammer...")
                        effects.write("Du wirst erwischt und der Schule verwiesen.")
                        effects.game_over('Ende 3')
                        sys.exit()
                else:
                    effects.write("Dieses Item kann hier nicht verwendet werden.")

        elif yn == "3":
            effects.write("Du kehrst in die Eingangshalle zurrück...")
            main_hall()
            break

        else:
            print("Die Eingabe war ungültig.")


def basement():
    """
    Definiert die Logik für den Keller.
    Der Spieler muss sich vor Ratten schützen, kann Items aufnehmen oder zurückkehren.
    """
    room_intro(2)
    while True:
        effects.write("1. Items im aktuellen Raum anschauen, 2. Item verwenden, 3. Zurück in die Haupthalle")
        yn = input("1/2/3: ")
        effects.clear_screen()

        if yn == "1":
            if "Ratten" in basement_inv:
                effects.write("Du stolperst über einige Ratten und wirst gebissen!")
                effects.game_over('Ende 4')
                sys.exit()

            # Logik zum Aufnehmen von Items.
            while True:
                effects.write("Du findest folgende Items:")
                pos = 1
                for item in basement_inv:
                    effects.write(f"{pos}. {item}")
                    pos += 1
                print()
                effects.write(f"{pos}. Zurrück")
                if not basement_inv:
                    effects.write("Keine weiteren Items hier.")
                    break

                if input("Item aufnehmen? (Y/n): ") == "Y":
                    choice = input("Nummer des Items: ")
                    if choice.isdigit() and 0 < int(choice) <= len(basement_inv):
                        item_taken = basement_inv.pop(int(choice) - 1)
                        player_inv.append(item_taken)
                        effects.write(f"Du nimmst: {item_taken}")
                    else:
                        effects.write("Ungültige Auswahl.")
                else:
                    break

        elif yn == "2":
            # Logik zur Verwendung von Rattenspray.
            effects.write("Welches Item verwenden?")
            pos = 1
            for item in player_inv:
                 effects.write(f"{pos}. {item}" + (" (Kann verwendet werden!)" if item == "Rattenspray" else ""))
                 pos += 1
            print()
            effects.write(f"{pos}. Zurrück")

            choice = input("Nummer: ")
            if choice.isdigit() and 0 < int(choice) <= len(player_inv):
                if player_inv[int(choice) - 1] == "Rattenspray":
                    if input("Rattenspray verwenden? (Y/n): ") == "Y":
                        effects.write("Du sprühst wie ein Irrer...")
                        effects.write("Alle Ratten sind geflohen!")
                        basement_inv.remove("Ratten")
                else:
                    effects.write("Das kannst du hier nicht verwenden.")

        elif yn == "3":
            effects.write("Du kehrst in die Eingangshalle zurrück...")
            main_hall()
            break

        else:
            print("Ungültige Eingabe.")


def main_hall():
    """
    Definiert die Logik für die Haupthalle.
    Dies ist der zentrale Knotenpunkt, von dem aus andere Räume betreten werden können.
    """
    effects.write("Was möchtest du tun?")
    while True:
        effects.write("1. Items im aktuellen Raum anschauen, 2. Andere Räume betreten")
        yn = input("1/2: ")
        effects.clear_screen()

        if yn == "1":
            # Logik zum Aufnehmen von Items.
            while True:
                effects.write("Du findest:")
                pos = 1
                for item in main_hall_inv:
                    effects.write(f"{pos}. {item}")
                    pos += 1
                print()
                effects.write(f"{pos}. Zurrück")
                if not main_hall_inv:
                    effects.write("Keine Items mehr hier.")
                    break

                if input("Item aufnehmen? (Y/n): ") == "Y":
                    choice = input("Nummer: ")
                    if choice.isdigit() and 0 < int(choice) <= len(main_hall_inv):
                        item_taken = main_hall_inv.pop(int(choice) - 1)
                        player_inv.append(item_taken)
                        effects.write(f"Du nimmst: {item_taken}")
                    else:
                        effects.write("Ungültige Auswahl.")
                else:
                    break

        elif yn == "2":
            # Navigation zu anderen Räumen.
            effects.write("Welchen Raum möchtest du betreten?")
            effects.write("1. Lehrerzimmer, 2. Requisiten Keller, 3. Serverraum")
            room_choice = input("1/2/3: ")
            if room_choice == "1":
                teacher()
                break
            elif room_choice == "2":
                basement()
                break
            elif room_choice == "3":
                server_room()
                break
            else:
                effects.write("Ungültige Auswahl.")

        else:
            print("Ungültige Eingabe.")


def outside():
    """
    Startpunkt des Spiels.
    Der Spieler muss die Tür knacken oder aufbrechen, um ins Innere zu gelangen.
    """
    effects.write("Du startest vor dem Schulgebäude...")
    effects.write("Du stehst vor der Tür des Haupteingangs.")
    effects.write("Zum Glück hast du dies bedacht und 5 Ditriche Mitgenommen.")

    lockpicks = 5
    while True:
        yn = input("Versuchen das Schloss zu knacken? (Y/n): ")
        effects.clear_screen()

        if yn == "Y":
            effects.write("Zum knacken des Schlosses errate die Zahl von 1-5 in 2 Versuchen.")
            is_success = functions.door_lock(lockpicks)

            if is_success == 777:
                functions.main_door()
                break
            else:
                lockpicks -= 1
                if lockpicks == 0:
                    effects.write("Dir sind die Ditriche ausgegangen Q_Q.")
                    if input("Möchtest du stattdessen die Tür aufbrechen? (Y/n): ") == "Y":
                        if functions.percent(80) == 1:
                            effects.write("Du hast es geschafft die Tür aufzubrechen!")
                            functions.main_door()
                            break
                        else:
                            effects.write("Der Hausmeister hat den Knall gehört und die Polizei gerufen :c")
                            effects.game_over('Ende 2')
                            sys.exit()
                    else:
                        effects.game_over('Ende 1')
                        sys.exit()

        elif yn == "n":
            effects.write("Du entscheidest dich dafür, doch nicht in die Schule einzubrechen.")
            effects.game_over('Ende 0')
            break

        else:
            print("Ungültige Eingabe.")
