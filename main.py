from datetime import datetime, timedelta
import time
import threading
import pygame
from pynput import keyboard

paused = False  # Indicator to know if the clock is paused
stop_program = False  # Indicator to stop the program


def choice():
    #Select the clock format
    try:
        hour_format = input("\nPlease select the clock format: \n12h: '12' \n24h: '24'\n ")
        if hour_format == "12":
            return "%I:%M:%S %p"  # 12h format with AM/PM
        elif hour_format == "24":
            return "%H:%M:%S"  # 24h format
        else:
            print("Invalid format. The 24h format will be used by default.")
            return "%H:%M:%S"
    except KeyboardInterrupt:
        print("\nReturn to menu.")
        return "%H:%M:%S"


def toggle_pause():
    #Pause or resume clock
    global paused
    paused = not paused
    print("\nPause" if paused else "\nResume")


def increment_time(new_time_ref):
    #Increments time continuously by one second
    global paused
    while not stop_program:
        if not paused:
            new_time_ref[0] += timedelta(seconds=1)
            time.sleep(1)


def display_time(hour_format, current_time, alarm_timer):
    #Displays actual time
    formatted_time = current_time.strftime(hour_format)
    print(f'\r{formatted_time}', end="")

    # Checks the alarm 
    if alarm_timer and formatted_time == alarm_timer:
        print("\nThe alarm has rung !")
        play_sound("3046.mp3")
        return None  # Resets the alarm after it has rung

    return alarm_timer


def play_sound(file_path):
    #Play a sound with pygame
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"Error while reading audio file : {e}")


def manage_clock(hour_format, new_time_ref, alarm_timer):
    # Manages the continuous display of the clock 
    global stop_program

    def on_press(key):
        #Manages keyboard entry with pynput
        global stop_program, paused
        try:
            if key.char == 'p':
                toggle_pause()
        except AttributeError:
            pass

    # Set up the listener for keyboard entry 
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        while not stop_program:
            # Synchronize the access to new_time
            current_time = new_time_ref[0]

            # Clock display
            alarm_timer = display_time(hour_format, current_time, alarm_timer)

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nReturn to menu.")
    finally:
        listener.stop()


def time_setting(hour_format):
    #Set a new time
    try:
        new_time_input = input("Enter the time in format HH:MM:SS or L for local time : ")
        if new_time_input.upper() == "L":
            return datetime.now()
        else:
            return datetime.strptime(new_time_input, "%H:%M:%S")
    except ValueError:
        print("Invalid format. Please be sure to use HH:MM:SS.")
        return time_setting(hour_format)


def alarm_setting():
    #Set an alarm
    try:
        alarm_input = input("Set the alarm with format HH:MM:SS : ")
        return alarm_input
    except KeyboardInterrupt:
        print("\nReturn to menu.")
        return None


def menu():
    #Main menu display
    return input("\nWhat would you like to do? \n1. Display the time \n2. Set the time \n3. Set an alarm \n4. Change the time format \nYour choice : ").strip()


def main(hour_format, new_time_ref, alarm_timer):
    #Loop to run main program
    global stop_program

    while not stop_program:
        try:
            set_time = menu()

            if set_time == "1":
                # Display time 
                manage_clock(hour_format, new_time_ref, alarm_timer)

            elif set_time == "2":
                # Set a new time
                new_time_ref[0] = time_setting(hour_format)

            elif set_time == "3":
                # Set an alarm
                alarm_timer = alarm_setting()

            elif set_time == "4":
                # Change clock format
                hour_format = choice()

            else:
                print("Invalid choice. Please try again.")

        except KeyboardInterrupt:
            print("\nUse the menu to quit the program.")
            stop_program = True


if __name__ == "__main__":
    hour_format = "%H:%M:%S"  # Default format
    new_time = [datetime.strptime("00:00:00", "%H:%M:%S")]  # HDefault time (list to make it amendable)
    alarm_timer = None

    # Start the thread to increment the time
    threading.Thread(target=increment_time, args=(new_time,), daemon=True).start()

    # Launch main program
    main(hour_format, new_time, alarm_timer)