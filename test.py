from datetime import datetime, timedelta
import time
import keyboard 
import playsound


def main():
    # Demander le format d'heure à l'utilisateur
    hour_format = input("\nChoisissez le format d'heure: \n12h: '12' \n24h: '24'\n ")

    # Vérification du format
    if hour_format not in ["12", "24"]:
        print("Format invalide. Par défaut, le format 24h sera utilisé.")
        hour_format = "24"

    # Définir le format d'affichage en fonction du choix
    if hour_format == "12":
        time_format = "%I:%M:%S %p"  # Format 12h avec AM/PM
    else:
        time_format = "%H:%M:%S"  # Format 24h

    # Saisie de l'action souhaitée
    set_time = input("Que souhaitez-vous faire ? \nAfficher l'heure (H) \nRégler l'heure (R) \nMettre une alarme (A) ")

    paused = False  # Indicateur pour savoir si l'horloge est en pause


    def toggle_pause():
        global paused
        paused = not paused


    # Affichage de l'heure en temps réel
    try:
        if set_time == "H":
            print("Appuyez sur 'p' pour mettre en pause ou reprendre.")
            while True:
                if not paused:  # Si l'horloge n'est pas en pause, afficher l'heure
                    now = datetime.now()
                    current_time = now.strftime(time_format)
                    print(f'\r{current_time}', end="")
                time.sleep(1)

                # Vérifier si la touche 'p' est pressée
                if keyboard.is_pressed('p'):  # Appuyer sur 'p' pour basculer l'état
                    toggle_pause()
    except KeyboardInterrupt:
        main()

        # Simulation d'une heure réglée
    try:
        if set_time == "R":
            new_time_input = input("Saisissez l'heure au format HH:MM:SS : ")
            try:
                new_time = datetime.strptime(new_time_input, "%H:%M:%S")
            except ValueError:
                print("Format invalide. Assurez-vous d'utiliser HH:MM:SS.")
                exit()

            print("Appuyez sur 'p' pour mettre en pause ou reprendre.")
            while True:
                if not paused:  # Si l'horloge n'est pas en pause, mettre à jour l'heure
                    current_time = new_time.strftime(time_format)
                    print(f'\r{current_time}', end="")
                    new_time += timedelta(seconds=1)
                time.sleep(1)

                # Vérifier si la touche 'p' est pressée
                if keyboard.is_pressed('p'):
                    toggle_pause()
    except KeyboardInterrupt:
        main()

        # Définir une alarme
    try:
        if set_time == "A":
            alarm = input("Set the alarm in format: 'HH:MM:SS': ")
            while True : 
                now = datetime.now()
                current_time = now.strftime('%H:%M:%S')
                time.sleep(1)
                print(f'\r{current_time}', end="\r")
                if current_time == alarm:
                    playsound.playsound("3046.mp3")
                    print("\n The alarm rang !")
    except KeyboardInterrupt: 
        main()
print(main()) 