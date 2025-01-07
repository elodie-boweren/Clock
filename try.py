from datetime import datetime, timedelta
import time
import keyboard 

def main():
    # Ask user for clock format
    hour_format = input("\nPlease select the time format you want: \n12h: '12' \n24h: '24' ")

    # format check
    if hour_format not in ["12", "24"]:
        print("Invalid format. the 24 hour format will be used by default.")
        hour_format = "24"

    # Define the clock format based on the option selected
    if hour_format == "12":
        time_format = "%I:%M:%S %p"  # 12h format with AM/PM
    else:
        time_format = "%H:%M:%S"  # 24h format

    # Choice selection 
    set_time = input("What would you like to do ? \nDisplay the clock (H) \nSet/change the time (R) \nSet an alarm (A) ")

    paused = False  # Indicator to know if clock is on pause


    def toggle_pause():
        global paused
        paused = not paused


    # Display clock on current time
    try:
        if set_time == "H":
            print("Long press 'p' to pause or resume.")
            while True:
                if not paused:  # If the clock is not on pause, display the time
                    now = datetime.now()
                    current_time = now.strftime(time_format)
                    print(f'\r{current_time}', end="")
                time.sleep(1)

                # Check if 'p' is pressed
                if keyboard.is_pressed('p'):  # Long press 'p' to change state
                    toggle_pause()
    except KeyboardInterrupt:
        main()

        # Simulation of preset time
    try:
        if set_time == "R":
            new_time_input = input("Enter the time following the format HH:MM:SS : ")
            try:
                new_time = datetime.strptime(new_time_input, "%H:%M:%S")
            except ValueError:
                print("Invalid format. Be sure to use HH:MM:SS.")
                exit()

            print("Long press 'p' to pause or resume.")
            while True:
                if not paused:  # If clock is not paused, update the time
                    current_time = new_time.strftime(time_format)
                    print(f'\r{current_time}', end="")
                    new_time += timedelta(seconds=1)
                time.sleep(1)

                # Check if 'p' is pressed
                if keyboard.is_pressed('p'):
                    toggle_pause()
    except KeyboardInterrupt:
        main()

        # Set an alarm
    try:
        if set_time == "A":
            alarm = input("Enter the time you would like tha alarm to ring following the format HH:MM:SS : ")
            try:
                alarm_time = datetime.strptime(alarm, "%H:%M:%S").time()
            except ValueError:
                print("Invalid format. Be sure to use HH:MM:SS.")
                exit()

            print("Long press 'p' to pause or resume.")
            while True:
                if not paused:  # If the clock is not on pause
                    now = datetime.now()
                    current_time = now.strftime(time_format)
                    print(f'\r{current_time}', end="")
                    if now.time() == alarm_time:
                        print("\nThe alarm has rung !")
                        break
                time.sleep(1)

                # Check if 'p' is pressed
                if keyboard.is_pressed('p'):
                    toggle_pause()

        else:
            print("Invalid choice.")
    except KeyboardInterrupt:
        main()
print(main())