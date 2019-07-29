import tkinter as tk

class Obstacle:
    def __init__(self, x, y, height, framerate, speed, bird_x):
        self.x = x
        self.y = y
        self.height = height
        self.ground = height / 10 * 8
        self.sprite = tk.PhotoImage(file='img/obstacle.gif')
        self.framerate = framerate
        self.speed = speed
        self.replaced = False
        self.bird_x = bird_x
        
        
    def logic(self):
        self.x -= self.speed / float(self.framerate)


    def check_collision(self, bbox):
        return self.x - 25 < bbox[2] and self.x + 25 > bbox[0] and \
               (self.y - 86 > bbox[1] or self.y + 86 < bbox[3])


    def render(self, canvas):
        # render the gates
        # gates are (86 * 2)px high and (45 * 2)px wide
        canvas.create_image(self.x, self.y, image=self.sprite)
        self.logic()
