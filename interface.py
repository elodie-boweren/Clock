from datetime import datetime, timedelta
import time
from tkinter import *

#creating an object
window = Tk()
window.minsize(300, 200)

#creating a title 
window.title("L'horloge de mamie")

border = Frame(window)

def main():
    #Choice
    title = Label(window, text = "What would you like to do?")
    print_time = Button(window, text = "Print time")
    set_time = Button(window, text = "Set time")
    set_alarm = Button(window, text="Set alarm") 
    print_time.pack()
    set_time.pack()
    set_alarm.pack()
    #printing the title
    title.pack()

    
    try :
        #loop to print time
        if print_time == True:
            while True :
                now = datetime.now()
                current_time = now.strftime('%H:%M:%S')
                time.sleep(1)

                print(f'\r{current_time}', end="\r")
    except KeyboardInterrupt: #Ctrl+C to go back to the main loop
        main()

    try:       
        if set_time == True:
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
        if set_alarm == True:
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


#Always at the end : starting the tkinter loop
window.mainloop()