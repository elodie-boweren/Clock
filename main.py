from datetime import datetime, timedelta
import time

def main():
    #Choice
    set_time = input("What would you like to do? \nPrint time (P) \nSet time (T) \nSet alarm (A) \nMake your choice: ")

    try :
        #loop to print time
        if set_time == "P":
            while True :
                now = datetime.now()
                current_time = now.strftime('%H:%M:%S')
                time.sleep(1)

                print(f'\r{current_time}', end="\r")
    except KeyboardInterrupt: #Ctrl+C to go back to the main loop
        main()

    try:       
        if set_time == "T":
            new_time_input = (input(f"set the time in format: 'HH:MM:SS': "))
            try:
                # Convert user input into datetime obect
                new_time = datetime.strptime(new_time_input, "%H:%M:%S")
            except ValueError:
                print("Wrong format! Make sure to use: 'HH:MM:SS'! ")
                exit()
            while True:   
                current_time = new_time.strftime('%H:%M:%S')  
                print(f'\r{current_time}', end="\r")
                time.sleep(1)
                new_time += timedelta(seconds=1)
    except KeyboardInterrupt:
        main()        
    
    try:
        if set_time == "A":
            alarm = input("Set the alarm in format: 'HH:MM:SS': ")
            while True : 
                now = datetime.now()
                current_time = now.strftime('%H:%M:%S')
                time.sleep(1)
                print(f'\r{current_time}', end="\r")
                if current_time == alarm:
                    print("\n The alarm rang !")
    except KeyboardInterrupt: 
        main()
print(main())