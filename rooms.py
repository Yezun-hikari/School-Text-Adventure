import functions
import effects
import time
import sys

server_room_inv = ["Netzwerkkabel", "Hammer"]
teacher_inv = ["Gas", "Regal", "Schreibtisch"]
main_hall_inv = ["Rattenspray", "Dietriche", "Verschimmelter Käse"]
basement_inv = ["Gasmaske", "Ratten", "Schaumstoff-Schwert"]
player_inv = []


def room_intro(room_id):
    if room_id == 1:
        if "Gas" in teacher_inv:
            effects.write("Sobald du das Lehrerzimmer betrittst sticht dir ein intensiver Kaffegeruch in die Nase.")
            effects.write("Ohne eine Gasmaske wirst du hier Schnell ersticken...")
            print()
            effects.write("Was möchtest du tun?")


        else:
            effects.write("Was möchtest du tun?")

    if room_id == 2:
        if "Ratten" in basement_inv:
            effects.write("Als du den Keller betrittst, hörst du sofort das nagen von Ratten.")
            effects.write("Ein Rattenspray währe eventuell gut...")
            print()
            effects.write("Was möchtest du tun?")


        else:
            effects.write("Was möchtest du tun?")



def teacher():
    room_intro(1)

    while True:
        effects.write("1. Nach Items im aktuellen Raum schauen, 2. Item verwenden, 3. Zurück in die Haupthalle")
        yn = input("1/2/3: ")
        effects.clear_screen()

        if yn == "1":
            if "Gas" in teacher_inv:
                effects.write("Du athmest zu viel vom Kaffegeruch ein und fällst zu Boden!")
                time.sleep(2)
                effects.game_over('Ende 5')
                sys.exit()

            else:
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

                        if item_choice == "":
                            effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Orte.")

                        elif int(item_choice) == len(teacher_inv) + 1:
                            effects.write("Kein Ort wird durchsucht.")
                            effects.clear_screen()
                            server_room()

                        elif 0 < int(item_choice) < len(teacher_inv) + 1:
                            item_choice = int(item_choice)
                            item_taken = teacher_inv[item_choice - 1]
                            class_test = functions.percent(50)
                            if item_taken == "Regal":
                                if class_test == 1:
                                    item_taken = "Klassenarbeiten"
                                    effects.write("Du hast die Klassenarbeiten im Regal gefunden!")
                                    effects.write("Du erzählst allen von deinem Erfolg und wirst als Held gefeiert!")
                                else:
                                    effects.write("Das Regal ist leer...")
                                    time.sleep(2)
                                    effects.write("ES QUITSCHT!")
                                    fifty = functions.percent(75)
                                    if fifty == 1:
                                        effects.write("Züm glück hat der Hausmeister nichts gehört.")

                                    else:
                                        effects.write("Der Hausmeister hat das Quietschen gehört und die Polizei gerufen :/")
                                        time.sleep(2)
                                        effects.game_over('Ende 6')
                                        sys.exit()

                            if item_taken == "Schreibtisch":
                                if class_test == 0:
                                    item_taken = "Klassenarbeiten"
                                    effects.write("Du hast die Klassenarbeiten im Schreibtisch gefunden!")
                                    effects.write("Du erzählst allen von deinem Erfolg und wirst als Held gefeiert!")
                                else:
                                    effects.write("Der Schreibtisch ist leer...")
                                    time.sleep(2)
                                    effects.write("ES QUITSCHT!")
                                    fifty = functions.percent(75)
                                    if fifty == 1:
                                        effects.write("Züm glück hat der Hausmeister nichts gehört.")

                                    else:
                                        effects.write("Der Hausmeister hat das Quietschen gehört und die Polizei gerufen :/")
                                        time.sleep(2)
                                        effects.game_over('Ende 6')
                                        sys.exit()


                        else:
                            effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Orte.")

                    elif yn == "n":
                        effects.clear_screen()
                        effects.write("Es wird an keinem Ort gesucht.")
                        teacher()

                    else:
                        print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

        elif yn == "2":
            effects.write("Welches Item soll verwendet werden?")
            effects.write("Du wühlst in deiner Tasche rum und findest folgende Items:")
            pos = 1
            for item in player_inv:
                if item == "Gasmaske":
                    effects.write(str(pos) + ". " + item + " (Kann verwendet werden!)")
                    pos = pos + 1
                else:
                    effects.write(str(pos) + ". " + item)
                    pos = pos + 1
            print()
            effects.write(str(pos) + ". Zurrück")

            while True:
                item_use = input("Nummer des Items: ")
                effects.clear_screen()

                if item_use == "":
                    effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

                elif int(item_use) == len(player_inv) + 1:
                    effects.write("Kein Item wird verwendet.")
                    effects.clear_screen()
                    teacher()

                elif 0 < int(item_use) < len(player_inv) + 1:
                    item_use = int(item_use)
                    item_used = player_inv[item_use - 1]

                    if item_used == "Gasmaske":
                        while True:
                            effects.write("Gasmaske anziehen, um dem Kaffegeruch entgegen zu stehen?")
                            yn = input("Y/n: ")
                            
                            if yn == "Y":
                                effects.write("Du ziehst dir so schnell wie möglich die Gasmaske an...")
                                effects.write("Du holst tief Luft und kannst dich wieder frei Bewegen!")
                                teacher_inv.remove("Gas")
                                player_inv.remove("Gasmaske")
                                time.sleep(2)
                                effects.clear_screen()
                                teacher()

                            elif yn == "n":
                                effects.write("Du entscheidest dich dagegen die Gasmaske anzuziehen.")
                                time.sleep(1)
                                effects.clear_screen()
                                teacher()

                            else:
                                print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

                    else:
                        effects.write("Das Item " + item_used + " kann hier nicht verwendet werden.")
                        time.sleep(1)
                        effects.clear_screen()
                        teacher()

                else:
                    effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

        elif yn == "3":
            effects.write("Du kehrst in die Eingangshalle zurrück...")
            effects.clear_screen()
            main_hall()

        else:
            print("Die Eingabe war ungültig, schreibe 1, 2 oder 3.")


def server_room():
    effects.write("Was möchtest du tun?")

    while True:
        effects.write("1. Items im aktuellen Raum anschauen, 2. Item verwenden, 3. Zurück in die Haupthalle")
        yn = input("1/2/3: ")
        effects.clear_screen()

        if yn == "1":
            while True:
                effects.write("Du schaust dich im Raum um und findest folgende Items:")
                pos = 1
                for item in server_room_inv:
                    effects.write(str(pos) + ". " + item)
                    pos = pos + 1
                print()
                effects.write(str(pos) + ". Zurrück")
                effects.write("Möchtest du eines der Items aufnehmen?")
                yn = input("Y/n: ")

                if yn == "Y":
                    effects.write("Welches Item möchtest du aufnehmen?")
                    item_choice = input("Nummer des Items: ")
                    effects.clear_screen()

                    if item_choice == "":
                        effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

                    elif int(item_choice) == len(server_room_inv) + 1:
                        effects.write("Kein Item wird aufgenommen.")
                        effects.clear_screen()
                        server_room()

                    elif 0 < int(item_choice) < len(server_room_inv) + 1:
                        item_choice = int(item_choice)
                        item_taken = server_room_inv[item_choice - 1]
                        effects.write("Du nimmst das Item: " + item_taken)
                        global player_inv
                        player_inv.append(item_taken)
                        server_room_inv.remove(item_taken)
                        time.sleep(1)
                        effects.clear_screen()
                        server_room()

                    else:
                        effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

                elif yn == "n":
                    effects.clear_screen()
                    effects.write("Kein Item wird aufgenommen.")
                    server_room()

                else:
                    print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

        elif yn == "2":
            effects.write("Welches Item soll verwendet werden?")
            effects.write("Du wühlst in deiner Tasche rum und findest folgende Items:")
            pos = 1
            for item in player_inv:
                if item == "Hammer":
                    effects.write(str(pos) + ". " + item + " (Kann verwendet werden!)")
                    pos = pos + 1
                else:
                    effects.write(str(pos) + ". " + item)
                    pos = pos + 1
            print()
            effects.write(str(pos) + ". Zurrück")

            while True:
                item_use = input("Nummer des Items: ")
                effects.clear_screen()

                if item_use == "":
                    effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

                elif int(item_use) == len(player_inv) + 1:
                    effects.write("Kein Item wird verwendet.")
                    effects.clear_screen()
                    server_room()

                elif 0 < int(item_use) < len(player_inv) + 1:
                    item_use = int(item_use)
                    item_used = player_inv[item_use - 1]

                    if item_used == "Hammer":
                        while True:
                            effects.write("Hammer verwenden um den Server zu zerstören?")
                            yn = input("Y/n: ")
                            
                            if yn == "Y":
                                effects.write("Du Zerstörst den Schulserver mit einem Hammer...")
                                effects.write("Du wirst erwischt und der Schule verwiesen.")
                                time.sleep(3)
                                effects.game_over('Ende 3')
                                sys.exit()

                            elif yn == "n":
                                effects.write("Du entscheidest dich dagegen den Server zu zerstören.")
                                time.sleep(1)
                                effects.clear_screen()
                                server_room()

                            else:
                                print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

                    else:
                        effects.write("Das Item " + item_used + " kann hier nicht verwendet werden.")
                        time.sleep(1)
                        effects.clear_screen()
                        server_room()

                else:
                    effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

        elif yn == "3":
            effects.write("Du kehrst in die Eingangshalle zurrück...")
            effects.clear_screen()
            main_hall()

        else:
            print("Die Eingabe war ungültig, schreibe 1, 2 oder 3.")


def basement():
    room_intro(2)

    while True:
        effects.write("1. Items im aktuellen Raum anschauen, 2. Item verwenden, 3. Zurück in die Haupthalle")
        yn = input("1/2/3: ")
        effects.clear_screen()

        if yn == "1":
            if "Ratten" in basement_inv:
                effects.write("Du stolperst über einige Ratten und wirst gebissen!")
                time.sleep(2)
                effects.game_over('Ende 4')
                sys.exit()

            else:
                while True:
                    effects.write("Du schaust dich im Raum um und findest folgende Items:")
                    pos = 1
                    for item in basement_inv:
                        effects.write(str(pos) + ". " + item)
                        pos = pos + 1
                    print()
                    effects.write(str(pos) + ". Zurrück")
                    effects.write("Möchtest du eines der Items aufnehmen?")
                    yn = input("Y/n: ")

                    if yn == "Y":
                        effects.write("Welches Item möchtest du aufnehmen?")
                        item_choice = input("Nummer des Items: ")
                        effects.clear_screen()

                        if item_choice == "":
                            effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

                        elif int(item_choice) == len(basement_inv) + 1:
                            effects.write("Kein Item wird aufgenommen.")
                            effects.clear_screen()
                            server_room()

                        elif 0 < int(item_choice) < len(basement_inv) + 1:
                            item_choice = int(item_choice)
                            item_taken = basement_inv[item_choice - 1]
                            effects.write("Du nimmst das Item: " + item_taken)
                            global player_inv
                            player_inv.append(item_taken)
                            basement_inv.remove(item_taken)
                            time.sleep(1)
                            effects.clear_screen()
                            server_room()

                        else:
                            effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

                    elif yn == "n":
                        effects.clear_screen()
                        effects.write("Kein Item wird aufgenommen.")
                        server_room()

                    else:
                        print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

        elif yn == "2":
            effects.write("Welches Item soll verwendet werden?")
            effects.write("Du wühlst in deiner Tasche rum und findest folgende Items:")
            pos = 1
            for item in player_inv:
                if item == "Rattenspray":
                    effects.write(str(pos) + ". " + item + " (Kann verwendet werden!)")
                    pos = pos + 1
                else:
                    effects.write(str(pos) + ". " + item)
                    pos = pos + 1
            print()
            effects.write(str(pos) + ". Zurrück")

            while True:
                item_use = input("Nummer des Items: ")
                effects.clear_screen()

                if item_use == "":
                    effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

                elif int(item_use) == len(player_inv) + 1:
                    effects.write("Kein Item wird verwendet.")
                    effects.clear_screen()
                    server_room()

                elif 0 < int(item_use) < len(player_inv) + 1:
                    item_use = int(item_use)
                    item_used = player_inv[item_use - 1]

                    if item_used == "Rattenspray":
                        while True:
                            effects.write("Rattenspray verwenden, um die Ratten zu verscheuchen?")
                            yn = input("Y/n: ")
                            
                            if yn == "Y":
                                effects.write("Du sprühst wie ein irrer mit deinem Rattenspray rum...")
                                effects.write("Alle Ratten sind geflohen - keine Gefahr mehr >:]")
                                basement_inv.remove("Ratten")
                                time.sleep(2)
                                effects.clear_screen()
                                basement()

                            elif yn == "n":
                                effects.write("Du entscheidest dich dagegen den Server zu zerstören.")
                                time.sleep(1)
                                effects.clear_screen()
                                basement()

                            else:
                                print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

                    else:
                        effects.write("Das Item " + item_used + " kann hier nicht verwendet werden.")
                        time.sleep(1)
                        effects.clear_screen()
                        basement()

                else:
                    effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

        elif yn == "3":
            effects.write("Du kehrst in die Eingangshalle zurrück...")
            effects.clear_screen()
            main_hall()

        else:
            print("Die Eingabe war ungültig, schreibe 1 oder 2.")


def main_hall():
    effects.write("Was möchtest du tun?")

    while True:
        effects.write("1. Items im aktuellen Raum anschauen, 2. Andere Räume betreten")
        yn = input("1/2: ")
        effects.clear_screen()

        if yn == "1":
            while True:
                effects.write("Du schaust dich im Raum um und findest folgende Items:")
                pos = 1
                for item in main_hall_inv:
                    effects.write(str(pos) + ". " + item)
                    pos = pos + 1
                print()
                effects.write(str(pos) + ". Zurrück")
                effects.write("Möchtest du eines der Items aufnehmen?")
                yn = input("Y/n: ")

                if yn == "Y":
                    effects.write("Welches Item möchtest du aufnehmen?")
                    item_choice = input("Nummer des Items: ")
                    effects.clear_screen()

                    if item_choice == "":
                        effects.clear_screen()
                        effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

                    elif int(item_choice) == len(main_hall_inv) + 1:
                        effects.write("Kein Item wird aufgenommen.")
                        effects.clear_screen()
                        main_hall()

                    elif 0 < int(item_choice) < len(main_hall_inv) + 1:
                        item_choice = int(item_choice)
                        item_taken = main_hall_inv[item_choice - 1]
                        effects.write("Du nimmst das Item: " + item_taken)
                        global player_inv
                        player_inv.append(item_taken)
                        main_hall_inv.remove(item_taken)
                        effects.clear_screen()
                        main_hall()

                    else:
                        effects.write("Die Eingabe war ungültig, wähle die Nummer eines der Items.")

                elif yn == "n":
                    effects.clear_screen()
                    effects.write("Kein Item wird aufgenommen.")
                    main_hall()

                else:
                    print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")


        elif yn == "2":
            while True:
                effects.write("Welchen Raum möchtest du betreten?")
                effects.write("1. Lehrerzimmer, 2. Requisiten Keller, 3. Serverraum")
                yn = input("1/2/3: ")
                effects.clear_screen()

                if yn == "1":
                    effects.write("Du gehst in  das Lehrerzimmer...")
                    effects.clear_screen()
                    teacher()

                elif yn == "2":
                    effects.write("Du gehst in den Requisiten Keller...")
                    effects.clear_screen()
                    basement()

                elif yn == "3":
                    effects.write("Du gehst in den Serverraum...")
                    effects.clear_screen()
                    server_room()

                else:
                    print("Die Eingabe war ungültig, schreibe die Zahl des Raumes.")

        else:
            print("Die Eingabe war ungültig, schreibe 1 oder 2.")


def outside():
    effects.write("Du startest vor dem Schulgebäude...")
    effects.write("Du stehst vor der Tür des Haupteingangs.")
    effects.write("Zum Glück hast du dies bedacht und 5 Ditriche Mitgenommen.")
    while True:
        effects.write("Versuchen das Schloss zu knacken?")
        yn = input("Y/n: ")
        effects.clear_screen()

        if yn == "Y":
            lockpicks = 5
            effects.write("Zum knacken des Schlosses errate die Zahl von 1-5 in 2 Versuchen.")
            while True:
                is_succes = functions.door_lock(lockpicks)
                if lockpicks == 1:
                    effects.write("Dir sind die Ditriche ausgegangen Q_Q.")
                    effects.write("Möchtest du stattdessen die Tür aufbrechen?")
                    yn = input("Y/n: ")
                    effects.clear_screen()
                    if yn == "Y":
                        effects.write("Du nimmst Anlauf und stößt mit voller kraft gegen die Tür...")

                        if functions.percent(80) == 1:
                            effects.write("Du hast es geschafft die Tür aufzubrechen, ohne, dass dich jeman gehört hat.")
                            functions.main_door()


                        else:
                            effects.write("Der Hausmeister hat den Knall gehört und die Polizei gerufen :c")
                            effects.game_over('Ende 2')
                            sys.exit()

                    elif yn == "n":
                        effects.write("Nach reichlicher Überlegung, hast du dich dafür enschieden es nicht zu tun.")
                        effects.write("Dir war das Risiko erwischt zu werden zu hoch.")
                        effects.game_over('Ende 1')
                        sys.exit()

                    else:
                        print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")

                if is_succes == 777:
                    functions.main_door()

                if is_succes == 6:
                    lockpicks = lockpicks - 1
                    effects.clear_screen()


        elif yn == "n":
            effects.write("Du entscheidest dich dafür, doch nicht in die Schule enzubrechen.")
            time.sleep(1)
            effects.game_over('Ende 0')
            return

        else:
            print("Die Eingabe war ungültig, schreibe Y oder n und achte auf die groß/kleinschreibung.")
