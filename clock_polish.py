from datetime import datetime, timedelta
import time


def menu():
    return input("What would you like to do? \
                    \nPrint Time (P) \
                    \nSet time (T) \
                    \nSet alarm (A) \
                    \nHour format (R) \
                    \nMake your choice: ")
    


def choice(hour_format):
    try:
        hour_choise = input("Choise format : 12 or 24")
        if hour_choise == "24":
            hour_format = "%H:%M:%S"
            return hour_format

        elif hour_choise == "12":
            hour_format = "%I:%M:%S %p"
            return hour_format
        
    except KeyboardInterrupt:
        print("\n return to menu")
        main(hour_format,new_time,alarm_timer)
        

def hour_parameter (hour_format, new_time):
    try:       
        new_time_input = input("set the time in format: 'HH:MM:SS': or 'HH:MM:SS AM/PM'")
        
        try:
            # Convertir l'entrée utilisateur en un objet datetime
            new_time = datetime.strptime(new_time_input, hour_format)
            return new_time
        
        except ValueError:
            print("Wrong format! Make sure to use: 'HH:MM:SS'! ")
            hour_parameter(hour_format, new_time)

    except KeyboardInterrupt:
        print("\n return to menu")
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
        print("\n return to menu")
        main(hour_format,new_time,alarm_timer)

def alarm_parameter(alarm_timer):
                
    try:
        alarm_timer = input("Set the alarm in format: 'HH:MM:SS': ")
        return alarm_timer
        
    except KeyboardInterrupt: 
        menu()


def main(hour_format,new_time,alarm_timer):
   
    while True:

        #Choice
        set_time = menu()
        
        # loop for hour format 
        if set_time == "R":
            hour_format = choice(hour_format) 

        elif set_time == "T":
            new_time = hour_parameter(hour_format, new_time)

        elif set_time == "P":
            print_hour(hour_format,new_time,alarm_timer)

        elif set_time == "A":
            alarm_timer = alarm_parameter(alarm_timer)
    


if __name__ == "__main__": 
    hour_format = "%H:%M:%S"  # Default hour format
    new_time = datetime.strptime("00:00:00", "%H:%M:%S")  # Default timemain()
    alarm_timer = "99:99:99"
    main(hour_format,new_time,alarm_timer)

    

 
