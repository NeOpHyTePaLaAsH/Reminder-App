#Importing required modules

from plyer import notification
import time
import sys
import tkinter as tk

# A normal banner

banner2 = '''

####################################################################################################
#                               Reminder App                                                       #
####################################################################################################
'''

#Printing the banner and asking required details in a function with some error handling

print(banner2)

try:

    def mainThing(time5, task5):

        #converting time into seconds from minutes

        time5 = time5 * 60

        print('\n')

        print('I will remind you after {} seconds'.format(time5))

        print('\n')

        time.sleep(time5)

        notification.notify( 
                    title = "Reminder", 
                    message=" Hey, it's a reminder : " + task5 , 
                    
                    # displaying time 
                    timeout=5 
        )

except Exception as error:
    sys.exit('An unexpected error occured: '+ error)

except KeyboardInterrupt:
    sys.exit('User ended the operation. Bye')

#Some global Variables

global timeNeeded
global taskToBeSheduled
global e1
global e2

#Some gui stuff

def do_some_things():
    timeNeeded = float(e2.get())
    taskToBeSheduled = e1.get()
    mainThing(timeNeeded, taskToBeSheduled)

master = tk.Tk()

master.geometry("220x100")
master.title("Reminder App")

tk.Label(master, text='Task :').grid(row=0)
tk.Label(master, text='Time in minutes :').grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1, padx=10)
e2.grid(row=1, column=1, padx=10)

tk.Button(master,
          text='Quit',
          command=master.quit
).grid(row=3,
       column=0,
       sticky=tk.W,
       pady=8,
       padx=10
)

tk.Button(master,
          text='Shedule',
          command=do_some_things
).grid(row=3,
       column=1,
       sticky=tk.W,
       pady=8,
)

master.resizable(False, False)

master.mainloop()