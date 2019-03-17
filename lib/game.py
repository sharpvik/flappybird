# STANDARD LIBRARY IMPORTS
import Tkinter as tk
from random import randint


# OWN IMPORTS
from lib.background import Background
from lib.ground import Ground
from lib.bird import Bird


class FlappyBird:
    def __init__(self):
        # DECLARE MAIN VARIBALES
        self.author = 'VIKTOR A. ROZENKO VOITENKO'
        self.version = 'ALPHA'
        self.on = False
        self.over = False
        self.framerate = 30 # pixels/second
        self.delay = 1000 / self.framerate # milliseconds
        self.screen_width = 990 # pixels
        self.screen_height = 600 # pixels
        self.bird = {
            'x'         : 200, # pixels
            'y'         : 240, # pixels
            'velocity'  : 0, # pixels/seconds
            'speed'     : 400, # pixels/second
        }
        self.g = 60 # pixels/second^2
        self.obstacle_spacing = 300 # pixels
        
        
        # GUI
        self.master = tk.Tk()
        self.master.tk.call('wm', 'iconphoto', self.master._w, 
                            tk.PhotoImage(file='img/icon.gif'))
        self.master.title('Flappy Bird')
        
        
        # OBJECTS
        self.background = Background(self.screen_width, self.screen_height)
        self.ground = Ground(self.screen_width, self.screen_height,
                             self.bird['speed'], self.framerate)
        self.flappy = Bird(self.bird['x'], self.bird['y'], 
                           self.bird['velocity'], self.g, self.framerate,
                           self.screen_height)
        
        
        # KEYPRESS DETECTION
        self.frame = tk.Frame(self.master, width=0, height=0)
        self.frame.bind('<KeyPress>', self.keypress_handler)
        self.frame.pack()
        self.frame.focus_set()
        
        
        self.canvas = tk.Canvas(self.master, width=self.screen_width, 
                                height=self.screen_height)
        self.canvas.pack()
        
        self.gameloop()
        
        self.master.mainloop()
        
    
    def keypress_handler(self, e):
        key = e.char.lower()
        if key == ' ':           # START / FLAP
            if not self.on:
                self.on = True
                self.gameloop()
            self.flappy.flap()
        elif key == 'p':         # PAUSE
            self.on = False
        elif key == 'r':         # RESUME
            if not self.on:
                self.on = True
                self.gameloop()
        elif key == 'q':         # QUIT
            quit()
        
        
    def gameloop(self):
        self.canvas.delete(tk.ALL) # clear canvas
        
        # render stuff
        self.background.render(self.canvas)
        self.flappy.render(self.canvas)
        self.ground.render(self.canvas)
        
        if self.on: # if GAME is not PAUSED
            self.master.after(self.delay, self.gameloop) # continue gameloop
