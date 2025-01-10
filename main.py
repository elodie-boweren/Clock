from datetime import datetime, timedelta
import time
import threading
import pygame
from pynput import keyboard

paused = False  # Indicateur pour savoir si l'horloge est en pause
stop_program = False  # Indicateur pour arrêter le programme


def choice():
    #Choisissez le format d'heure
    try:
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
    #Mettre en pause ou reprendre l'horloge
    global paused
    paused = not paused
    print("\nPause" if paused else "\nReprise")


def increment_time(new_time_ref):
    #Incrémente le temps d'une seconde en continu
    global paused
    while not stop_program:
        if not paused:
            new_time_ref[0] += timedelta(seconds=1)
            time.sleep(1)


def display_time(hour_format, current_time, alarm_timer):
    #Affiche l'heure actuelle et vérifie l'alarme
    formatted_time = current_time.strftime(hour_format)
    print(f'\r{formatted_time}', end="")

    if alarm_timer and formatted_time == alarm_timer:
        print("\nL'alarme a sonné !")
        play_sound("3046.mp3")
        return None  # Réinitialiser l'alarme après son déclenchement

    return alarm_timer


def play_sound(file_path):
    #Joue un son avec pygame
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier audio : {e}")


def manage_clock(hour_format, new_time_ref, alarm_timer):
    #Gère l'affichage de l'heure en continu
    global stop_program

    def on_press(key):
        #Gestion des touches clavier avec pynput
        global stop_program, paused
        try:
            if key.char == 'p':
                toggle_pause()
            elif key.char == 'q':
                stop_program = True
                return False  # Stop the listener
        except AttributeError:
            pass

    # Configurer le listener pour les entrées clavier
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        while not stop_program:
            # Synchroniser l'accès à new_time
            current_time = new_time_ref[0]

            # Afficher l'heure
            alarm_timer = display_time(hour_format, current_time, alarm_timer)

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nRetour au menu.")
    finally:
        listener.stop()


def time_setting(hour_format):
    #Règle une nouvelle heure
    try:
        new_time_input = input("Saisissez l'heure au format HH:MM:SS ou L pour l'heure locale : ")
        if new_time_input.upper() == "L":
            return datetime.now()
        else:
            return datetime.strptime(new_time_input, "%H:%M:%S")
    except ValueError:
        print("Format invalide. Assurez-vous d'utiliser HH:MM:SS.")
        return time_setting(hour_format)


def alarm_setting():
    #Règle une alarme
    try:
        alarm_input = input("Réglez l'alarme au format HH:MM:SS : ")
        return alarm_input
    except KeyboardInterrupt:
        print("\nRetour au menu.")
        return None


def menu():
    #Affiche le menu principal
    return input("\nQue souhaitez-vous faire ? \n1. Afficher l'heure \n2. Régler l'heure \n3. Mettre une alarme \n4. Changer le format d'heure\nVotre choix : ").strip()


def main(hour_format, new_time_ref, alarm_timer):
    #Boucle principale du programme
    global stop_program

    while not stop_program:
        try:
            set_time = menu()

            if set_time == "1":
                # Afficher l'heure en continu
                manage_clock(hour_format, new_time_ref, alarm_timer)

            elif set_time == "2":
                # Régler une nouvelle heure
                new_time_ref[0] = time_setting(hour_format)

            elif set_time == "3":
                # Régler une alarme
                alarm_timer = alarm_setting()

            elif set_time == "4":
                # Changer le format d'heure
                hour_format = choice()

            else:
                print("Choix invalide. Réessayez.")

        except KeyboardInterrupt:
            print("\nUtilisez le menu pour quitter.")
            stop_program = True


if __name__ == "__main__":
    hour_format = "%H:%M:%S"  # Format par défaut
    new_time = [datetime.strptime("00:00:00", "%H:%M:%S")]  # Heure par défaut (liste pour rendre mutable)
    alarm_timer = None

    # Démarrer le thread pour incrémenter le temps
    threading.Thread(target=increment_time, args=(new_time,), daemon=True).start()

    # Lancer le programme principal
    main(hour_format, new_time, alarm_timer)