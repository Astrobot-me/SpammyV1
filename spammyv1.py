from pyautogui import *
from time import sleep
import progressbar


Spammy_Logo = """ _____                                         _   _ __  
/  ___|                                       | | | /  | 
\ `--. _ __   __ _ _ __ ___  _ __ ___  _   _  | | | `| | 
 `--. | '_ \ / _` | '_ ` _ \| '_ ` _ \| | | | | | | || | 
/\__/ | |_) | (_| | | | | | | | | | | | |_| | \ \_/ _| |_
\____/| .__/ \__,_|_| |_| |_|_| |_| |_|\__, |  \___/\___/
      | |                               __/ |            
      |_|                              |___/ """

print(Spammy_Logo)
print("!!________________________________________________________!!")
a = input('Please enter the message you want to spam:>')
b = int(input('Please enter the number of times you want to spam the message:>'))
c = float(input("Please enter the Delay(Time between Each Successive Messages:>"))
print("Open the Window in which you want to spam messages. before the program begins.\n The program will begin in 20 "
      "''seconds . Please wait .")
print("!!________________________________________________________!!")

widgets = [' [',
           progressbar.Timer(format='Spaming in Progress: %(elapsed)s'),
           '] ',
           progressbar.Bar('='), ' (',
           progressbar.ETA(), ') ',
           ]


while True:

    bar = progressbar.ProgressBar(max_value=b+1, widgets=widgets).start()
    sleep(20)
    for i in range(0, b):
        write(a)
        press('enter')
        sleep(c)
        bar.update(i+1)

    print('')
    option = input("Do you want to use this program Again(y/n) :>")
    if option.lower() == "y" or option.lower() == "yes":
        data_options = input("Do you want to Keep the Same data as Earlier (y/n)")
        if data_options.lower() == "y" or data_options.lower() == "yes":
            pass
        elif data_options.lower() == "n" or data_options.lower() == 'no':
            print("!!________________________________________________________!!")
            a = input("Please enter the message you want to spam:>")
            b = int(input("Please enter the number of times you want to spam the message:>"))
            c = float(input('Please enter the Delay(Time between Each Successive Messages:>'))
            print("!!________________________________________________________!!")

    elif option.lower() == "n" or option.lower() == "no":
        break
    else:
        print("Invalid Input Received !! Try Again")
