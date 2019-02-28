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
    'BIRD Y'        : 100, # pixels
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


frame = Tkinter.Frame(master, width=0, height=0)
frame.bind('<KeyPress>', flappy.flap)
frame.pack()
frame.focus_set()

canvas = Tkinter.Canvas(master, width=GAME['WIDTH'], height=GAME['HEIGHT'])
canvas.pack()


def render():
    canvas.delete(Tkinter.ALL) # clear canvas
    
    # render sky and ground
    canvas.create_rectangle(0, 0, GAME['WIDTH'], GAME['HEIGHT'] / 10 * 8,
                            fill='#42A5F5', outline='') 
    canvas.create_rectangle(0, GAME['HEIGHT'] / 10 * 8, 
                            GAME['WIDTH'], GAME['HEIGHT'], fill='#00BFA5',
                            outline='')
    
    flappy.render(canvas) # render flappy
    
    master.after(GAME['DELAY'], render) # render again after GAME['DELAY']

render()


master.mainloop()
