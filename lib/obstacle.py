import Tkinter

class Obstacle:
    def __init__(self, x, y, height, framerate, speed):
        self.x = x
        self.y = y
        self.height = height
        self.ground = height / 10 * 8
        self.sprite = Tkinter.PhotoImage(file='img/obstacle.gif')
        self.framerate = framerate
        self.speed = speed
        self.replaced = False
        
    def logic(self):
        self.x -= self.speed / float(self.framerate)
        
    def render(self, canvas):
        # render the gates
        # gates are 243px high
        canvas.create_image(self.x, self.y, image=self.sprite)
        self.logic()
