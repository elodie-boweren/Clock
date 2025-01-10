from datetime import datetime, timedelta
import time
import keyboard
import playsound
import threading

paused = False  # Indicateur pour savoir si l'horloge est en pause

def choice():
    try:
        # Demander le format d'heure à l'utilisateur
        hour_format = input("\nChoisissez le format d'heure: \n12h: '12' \n24h: '24'\n ")

        if hour_format == "12":
            return "%I:%M:%S %p"  # Format 12h avec AM/PM
        elif hour_format == "24":
            return "%H:%M:%S"  # Format 24h
        else:
            print("Format invalide. Par défaut, le format 24h sera utilisé.")
            return "%H:%M:%S"
    except KeyboardInterrupt:
        print("\nRetour au menu.")
        return "%H:%M:%S"


def toggle_pause():
    global paused
    paused = not paused


def print_hour(hour_format, new_time, alarm_timer):
    try:
        while True:
            if not paused:  # Si l'horloge n'est pas en pause
                current_time = new_time.strftime(hour_format)
                print(f'\r{current_time}', end="")
                time.sleep(1)
                new_time += timedelta(seconds=1)

                # Vérifier si l'heure actuelle correspond à l'alarme
                if alarm_timer and new_time.strftime("%H:%M:%S") == alarm_timer:
                    print("\nL'alarme a sonné!")
                    playsound.playsound("3046.mp3")
                    alarm_timer = None  # Réinitialiser l'alarme après son déclenchement

            # Vérifier si la touche 'p' est pressée pour mettre en pause
            if keyboard.is_pressed('p'):
                toggle_pause()
                print("\nPause" if paused else "\nReprise")
                time.sleep(0.5)  # Éviter les multiples détections
    except KeyboardInterrupt:
        print("\nRetour au menu.")
        main(hour_format, new_time, alarm_timer)

def clock():
    return print_hour(hour_format,new_time,alarm_timer)


def time_setting(hour_format):
    try:
        new_time_input = input("Saisissez l'heure au format HH:MM:SS ou L pour l'heure locale : ")
        if new_time_input.upper() == "L":
            return datetime.now()
        else:
            return datetime.strptime(new_time_input, "%H:%M:%S")
    except ValueError:
        print("Format invalide. Assurez-vous d'utiliser HH:MM:SS.")
        return time_setting(hour_format)
    except KeyboardInterrupt:
        print("\nRetour au menu.")
        main(hour_format, new_time, alarm_timer)


def alarm_setting():
    try:
        alarm_input = input("Réglez l'alarme au format HH:MM:SS : ")
        return alarm_input
    except KeyboardInterrupt:
        print("\nRetour au menu.")
        main(hour_format, new_time, alarm_timer)


def menu():
    return input("\nQue souhaitez-vous faire ? \n1. Afficher l'heure \n2. Régler l'heure \n3. Mettre une alarme \n4. Changer le format d'heure\nVotre choix : ")


def main(hour_format, new_time, alarm_timer):
    
    while True:
        set_time = menu()

        if set_time == "1":
            print_hour(hour_format, new_time, alarm_timer)
        elif set_time == "2":
            new_time = time_setting(hour_format)
        elif set_time == "3":
            alarm_timer = alarm_setting()
        elif set_time == "4":
            hour_format = choice()
        else:
            print("Choix invalide. Réessayez.")


if __name__ == "__main__":
    hour_format = "%H:%M:%S"  # Format par défaut
    new_time = datetime.strptime("00:00:00", "%H:%M:%S")  # Heure par défaut
    alarm_timer = None
    thread=threading.Thread(target=clock, daemon=True)
    thread.start()
    main(hour_format, new_time, alarm_timer)