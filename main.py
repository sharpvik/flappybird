# STANDARD LIBRARY IMPORTS
import Tkinter
from random import randint

# OWN MODULES IMPORTS
from lib.background import Background
from lib.ground import Ground
from lib.bird import Bird
from lib.obstacle import Obstacle



# MAIN VARIABLES
GAME = {
    'AUTHOR'            : 'VIKTOR A. ROZENKO VOITENKO',
    'VERSION'           : 'ALPHA',
    'ON'                : False,
    'OVER'              : False,
    'FRAME RATE'        : 50, # frames/second
    'DELAY'             : 1000 / 50, # milliseconds
    'WIDTH'             : 990, # pixels
    'HEIGHT'            : 600, # pixels
    'BIRD X'            : 200, # pixels
    'BIRD Y'            : 240, # pixels
    'BIRD SIZE'         : 30, # pixels
    'BIRD VELOCITY'     : 0, # pixels/second
    'BIRD SPEED'        : 350, # pixels/second
    'BIRD G'            : 66, # pixels/second^2
    'OBSTACLE SPACING'  : 300, # pixels
}



# MAIN FUNCTIONS
def keypress_redirect(e):
    key = e.char.lower()
    if key == ' ':           # START / FLAP
        if not GAME['ON']:
            GAME['ON'] = True
            gameloop()
        flappy.flap()
    elif key == 'p':         # PAUSE
        GAME['ON'] = False
    elif key == 'r':         # RESUME
        if not GAME['ON']:
            GAME['ON'] = True
            gameloop()
    elif key == 'q':         # QUIT
        quit()
        
        
def logic():
    global GAME, obstacles
    # destroy invisible obstacle
    if obstacles[0].x < -50:
        obstacles.pop(0)
    # create new obstacle when needed
    if obstacles[-1].x <= GAME['WIDTH'] and not obstacles[-1].replaced:
        updated_x = obstacles[-1].x + GAME['OBSTACLE SPACING']
        random_y  = randint(132, 350)
        obstacles.append(
            Obstacle(updated_x, random_y, GAME['HEIGHT'], GAME['FRAME RATE'], 
                     GAME['BIRD SPEED'])
        )



# MAIN
    # GUI
master = Tkinter.Tk()


    # OBJECTS
background = Background(GAME['WIDTH'], GAME['HEIGHT'])
ground = Ground(GAME['WIDTH'], GAME['HEIGHT'], GAME['BIRD SPEED'],
                        GAME['FRAME RATE'])
flappy = Bird(GAME['BIRD X'], GAME['BIRD Y'], GAME['BIRD SIZE'], 
              GAME['BIRD VELOCITY'], GAME['BIRD G'], 
              GAME['FRAME RATE'], GAME['HEIGHT'])
obstacles = [
    Obstacle(GAME['WIDTH'] + 100, randint(132, 350), GAME['HEIGHT'], 
             GAME['FRAME RATE'], GAME['BIRD SPEED']),
]


# button press detection
frame = Tkinter.Frame(master, width=0, height=0)
frame.bind('<KeyPress>', keypress_redirect)
frame.pack()
frame.focus_set()


canvas = Tkinter.Canvas(master, width=GAME['WIDTH'], height=GAME['HEIGHT'])
canvas.pack()


def gameloop():
    logic()
    
    canvas.delete(Tkinter.ALL) # clear canvas
    
    # render stuff
    background.render(canvas)
    flappy.render(canvas)
    for obstacle in obstacles:
        obstacle.render(canvas)
    ground.render(canvas)
    
    if GAME['ON']: # if GAME is not PAUSED
        master.after(GAME['DELAY'], gameloop) # continue gameloop

gameloop()


master.mainloop()
