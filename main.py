# STANDARD LIBRARY IMPORTS
import Tkinter

# OWN MODULES IMPORTS
from lib.bird import Bird
from lib.obstacle import Obstacle



# MAIN VARIABLES
GAME = {
    'AUTHORS'       : ['VIKTOR A. ROZENKO VOITENKO', 'BENJAMIN A. MEDHURST',
                       'TUNG DO VIET', 'HENRIQUE CRUZ FONSECA'],
    'VERSION'       : 'ALPHA',
    'FRAME RATE'    : 50, # frames/second
    'DELAY'         : 1000 / 50, # milliseconds
    'WIDTH'         : 1000, # pixels
    'HEIGHT'        : 600, # pixels
    'BIRD X'        : 200, # pixels
    'BIRD Y'        : 50, # pixels
    'BIRD SIZE'     : 30, # pixels
    'BIRD VELOCITY' : 0, # pixels/second
    'BIRD G'        : 40, # pixels/second^2
}



# MAIN
    # OBJECTS
flappy = Bird(GAME['BIRD X'], GAME['BIRD Y'], GAME['BIRD SIZE'], 
              GAME['BIRD VELOCITY'], GAME['BIRD G'], 
              GAME['FRAME RATE'], GAME['HEIGHT'])
obstacles = list()

    # GUI
master = Tkinter.Tk()

canvas = Tkinter.Canvas(master, width=GAME['WIDTH'], height=GAME['HEIGHT'])
canvas.pack()


def render():
    canvas.delete(Tkinter.ALL) # clear canvas
    
    if flappy.y >= 500:
        flappy.flap()
    flappy.render(canvas) # render flappy
    
    master.after(GAME['DELAY'], render) # render again after GAME['DELAY']

render()


master.mainloop()
