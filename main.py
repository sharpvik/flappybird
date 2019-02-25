# STANDARD LIBRARY IMPORTS
from Tkinter import *
from time import sleep as delay

# OWN MODULES IMPORTS 
from lib.bird import Bird
from lib.obstacle import Obstacle



# MAIN VARIABLES
GAME = {
    'AUTHORS'       : ['VIKTOR A. ROZENKO VOITENKO', 'BENJAMIN A. MEDHURST', 
                       'TUNG DO VIET', 'HENRIQUE CRUZ FONSECA'],
    'VERSION'       : 'ALPHA',
    'FRAME RATE'    : 25,
    'DELAY'         : 1000 // 25,
    'WIDTH'         : 1000,
    'HEIGHT'        : 600,
}



# MAIN
flappy = Bird()
obstacles = list()

master = Tk()
canvas = Canvas(master, width=GAME['WIDTH'], height=GAME['HEIGHT'])
canvas.pack()
circle = canvas.create_oval(10, 10, 60, 60, fill='red')
canvas.pack()
delay(5)
master.mainloop()
delay(3)
canvas.move(circle, 50, 50)
canvas.update()
master.update()
