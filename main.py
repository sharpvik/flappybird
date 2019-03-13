# STANDARD LIBRARY IMPORTS
import Tkinter

# OWN MODULES IMPORTS
from lib.background import Background
from lib.bird import Bird
from lib.obstacle import Obstacle



# MAIN VARIABLES
GAME = {
    'AUTHORS'       : ['VIKTOR A. ROZENKO VOITENKO', 'BENJAMIN A. MEDHURST',
                       'TUNG DO VIET', 'HENRIQUE CRUZ FONSECA'],
    'VERSION'       : 'ALPHA',
    'ON'            : False,
    'OVER'          : False,
    'FRAME RATE'    : 50, # frames/second
    'DELAY'         : 1000 / 50, # milliseconds
    'WIDTH'         : 990, # pixels
    'HEIGHT'        : 600, # pixels
    'BIRD X'        : 200, # pixels
    'BIRD Y'        : 240, # pixels
    'BIRD SIZE'     : 30, # pixels
    'BIRD VELOCITY' : 0, # pixels/second
    'BIRD SPEED'    : 350, # pixels/second
    'BIRD G'        : 70, # pixels/second^2
}



# MAIN FUNCTIONS
def keypress_redirect(e):
    if e.char == ' ':           # START / FLAP
        if not GAME['ON']:
            GAME['ON'] = True
            gameloop()
        flappy.flap()
    elif e.char == 'p':         # PAUSE
        GAME['ON'] = False
    elif e.char == 'r':         # RESUME
        if not GAME['ON']:
            GAME['ON'] = True
            gameloop()
    elif e.char == 'q':         # QUIT
        quit()



# MAIN
    # GUI
master = Tkinter.Tk()


    # OBJECTS
background = Background(GAME['WIDTH'], GAME['HEIGHT'], GAME['BIRD SPEED'],
                        GAME['FRAME RATE'])
flappy = Bird(GAME['BIRD X'], GAME['BIRD Y'], GAME['BIRD SIZE'], 
              GAME['BIRD VELOCITY'], GAME['BIRD G'], 
              GAME['FRAME RATE'], GAME['HEIGHT'])
obstacles = [
    Obstacle(400, 350, GAME['HEIGHT'], GAME['FRAME RATE'], GAME['BIRD SPEED']),
    Obstacle(700, 350, GAME['HEIGHT'], GAME['FRAME RATE'], GAME['BIRD SPEED']),
    Obstacle(1000, 350, GAME['HEIGHT'], GAME['FRAME RATE'], GAME['BIRD SPEED']),
    Obstacle(1300, 350, GAME['HEIGHT'], GAME['FRAME RATE'], GAME['BIRD SPEED'])
]


# button press detection
frame = Tkinter.Frame(master, width=0, height=0)
frame.bind('<KeyPress>', keypress_redirect)
frame.pack()
frame.focus_set()


canvas = Tkinter.Canvas(master, width=GAME['WIDTH'], height=GAME['HEIGHT'])
canvas.pack()


def gameloop():
    canvas.delete(Tkinter.ALL) # clear canvas
    
    # render stuff
    background.render(canvas)
    flappy.render(canvas)
    for obstacle in obstacles:
        obstacle.render(canvas)
    
    if GAME['ON']: # if GAME is not PAUSED
        master.after(GAME['DELAY'], gameloop) # continue gameloop

gameloop()


master.mainloop()
