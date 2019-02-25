# STANDARD LIBRARY IMPORTS
import Tkinter
from time import sleep

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

master = Tkinter.Tk()

canvas = Tkinter.Canvas(master, width=GAME['WIDTH'], height=GAME['HEIGHT'])
canvas.pack()

x = 0

def repeat_me():
    global x
    canvas.delete(Tkinter.ALL)
    canvas.create_rectangle(x,50,x+50,50+50, fill = "yellow")
    x = x + 10
    master.after(1000, repeat_me)


repeat_me()

master.mainloop()
