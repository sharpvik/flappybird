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
    'FRAME RATE'    : 50,
    'DELAY'         : 1000 // 50,
    'WIDTH'         : 1000,
    'HEIGHT'        : 600,
    'BIRD X'        : 100,
    'BIRD Y'        : 50,
    'BIRD SIZE'     : 30,
    'BIRD VELOCITY' : 0,
    'BIRD G'        : 1,
}



# MAIN
flappy = Bird(GAME['BIRD X'], GAME['BIRD Y'], GAME['BIRD SIZE'], GAME['BIRD VELOCITY'], GAME['BIRD G'])
obstacles = list()

master = Tkinter.Tk()

canvas = Tkinter.Canvas(master, width=GAME['WIDTH'], height=GAME['HEIGHT'])
canvas.pack()

# this is just an example -- not real code
def render():
    canvas.delete(Tkinter.ALL)
    
    flappy.render(canvas)
    
    master.after(GAME['DELAY'], render)

render()
# example ends here -- everything else is real but incomplete :(

master.mainloop()
