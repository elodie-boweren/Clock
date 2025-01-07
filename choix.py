from datetime import datetime, timedelta
import time

# ask the time format
hour_format = input("What time format xould you want? \n12h: type '12'\n24h: type '24' \nYour choice: ")

# format check
if hour_format not in ["12", "24"]:
    print("Wrong format. The time will be set on 24h")
    hour_format = "24"

# Define print format
if hour_format == "12":
    time_format = "%I:%M:%S %p"  # Format 12h with AM/PM
else:
    time_format = "%H:%M:%S"  # Format 24h

#alarm choice
set_time = input("What would you like to do? \nPrint time (P) \nSet time (T) \nSet alarm (A) \nMake your choice: ")

#Loop to print time
if set_time == "P":
    while True :
        now = datetime.now()
        current_time = now.strftime(time_format)
        print(f'\r{current_time}', end="\r")
        time.sleep(1)
        
elif set_time == "T":
    new_time_input = (input(f"set the time in format: 'HH:MM:SS': "))
    try:
        # Convert user input into datetime obect
        new_time = datetime.strptime(new_time_input, "%H:%M:%S")
    except ValueError:
        print("Wrong format! Make sure to use: 'HH:MM:SS'! ")
        exit()
    while True:   
        current_time = new_time.strftime(time_format)  
        print(f'\r{current_time}', end="\r")
        time.sleep(1)
        new_time += timedelta(seconds=1)
    
elif set_time == "A":
    alarm = input("Set the alarm in format: 'HH:MM:SS': ")
    while True : 
        now = datetime.now()
        current_time = now.strftime(time_format)
        time.sleep(1)
        print(f'\r{current_time}', end="\r")
        if current_time == datetime.strptime(alarm, "%H:%M:%S").strftime(time_format):
            print("\n The alarm rang !")
            break
