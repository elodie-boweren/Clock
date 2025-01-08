from datetime import datetime, timedelta
import time


def menu():
    return input("What would you like to do? \
                    \nDisplay time (1) \
                    \nSet time (2) \
                    \nSet alarm (3) \
                    \nChange hour format (4) \
                    \nMake your selection: ")
    


def choice(hour_format):
    try:
        hour_choice = input("Choose format : 12 or 24 ")
        if hour_choice == "24":
            hour_format = "%H:%M:%S"
            return hour_format

        elif hour_choice == "12":
            hour_format = "%I:%M:%S %p"
            return hour_format
        
    except KeyboardInterrupt:
        print("\n Return to menu")
        main(hour_format,new_time,alarm_timer)
        

def time_setting (hour_format, new_time):
    try:       
        new_time_input = input("Set the time in format: 'HH:MM:SS': or 'HH:MM:SS AM/PM' or L for local time ")
        
        try:
            if new_time_input == "L":
                new_time = datetime.now()
                return new_time
            else:
            # Convert user input into datetime object
                new_time = datetime.strptime(new_time_input, hour_format)
                return new_time
        
        except ValueError:
            print("Wrong format! Make sure to use: 'HH:MM:SS'! ")
            time_setting(hour_format, new_time)

    except KeyboardInterrupt:
        print("\n Return to menu")
        main(hour_format,new_time,alarm_timer)



def print_hour(hour_format, new_time,alarm_timer):
    try :
        #loop to print time
        while True :
            current_time = new_time.strftime(hour_format)  
            print(f'\r{current_time}', end="\r")
            time.sleep(1)
            new_time += timedelta(seconds=1)
            if current_time == alarm_timer:
                print("\n The alarm rang !")
                    
    except KeyboardInterrupt: #Ctrl+C to go back to the main loop
        print("\n Return to menu")
        main(hour_format,new_time,alarm_timer)

def alarm_setting(alarm_timer):
                
    try:
        alarm_timer = input("Set the alarm in format: 'HH:MM:SS' or 'HH:MM:SS AM/PM' ")
        return alarm_timer
        
    except KeyboardInterrupt: 
        main(hour_format,new_time,alarm_timer)


def main(hour_format,new_time,alarm_timer):
   
    while True:

        #Choice
        set_time = menu()
        
        # loop for hour format 
        if set_time == "4":
            hour_format = choice(hour_format) 

        elif set_time == "2":
            new_time = time_setting(hour_format, new_time)

        elif set_time == "1":
            print_hour(hour_format,new_time,alarm_timer)

        elif set_time == "3":
            alarm_timer = alarm_setting(alarm_timer)
    


if __name__ == "__main__": 
    hour_format = "%H:%M:%S"  # Default hour format
    new_time = datetime.strptime("00:00:00", "%H:%M:%S")  # Default timemain()
    alarm_timer = "99:99:99"
    main(hour_format,new_time,alarm_timer)

    

 
