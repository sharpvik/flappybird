# STANDARD LIBRARY IMPORTS
import tkinter as tk
from random import randint


# OWN IMPORTS
from lib.background import Background
from lib.ground import Ground
from lib.bird import Bird
from lib.obstacle import Obstacle


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
            'speed'     : 200, # pixels/second
        }
        self.g = 55 # pixels/second^2
        self.obstacle_spacing = 300 # pixels
        self.collided = False
        
        
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
        self.obstacles = [
            Obstacle(self.screen_width + 100, randint(132, 350), 
                     self.screen_height, self.framerate, 
                     self.bird['speed'], self.bird['x']),
        ]
        
        
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
        
        
    def logic(self):
        # destoy invisible obstacle
        if self.obstacles[0].x < -50:
            self.obstacles.pop(0)
            
        # create new obstacle when needed
        if self.obstacles[-1].x <= self.screen_width and \
           not self.obstacles[-1].replaced:
            updated_x = self.obstacles[-1].x + self.obstacle_spacing
            random_y = randint(132, 350)
            self.obstacles.append(
                Obstacle(updated_x, random_y, self.screen_height,
                         self.framerate, self.bird['speed'], self.bird['x'])
            )        

    
    def gameloop(self):
        self.logic()
        self.canvas.delete(tk.ALL) # clear canvas
        
        # render stuff and detect collisions
        self.background.render(self.canvas)
        self.flappy.render(self.canvas)
        for obstacle in self.obstacles:
            obstacle.render(self.canvas)
            # detect collision with obstacles
            self.collided += obstacle.check_collision(self.flappy.bbox)
        self.ground.render(self.canvas)
        # detect collision with the ground
        self.collided += self.ground.check_collision(self.flappy.bbox)
        
        # GAME OVER on self.collided
        self.over = self.collided
        
        if self.on and not self.over: # if GAME is not PAUSED or OVER
            self.master.after( int(self.delay), self.gameloop ) # continue gameloop
