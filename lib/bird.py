import Tkinter


class Bird:
    def __init__(self, x, y, velocity, g, framerate, height):
        self.x = x
        self.y = y
        self.velocity = float(velocity)
        self.g = g
        self.framerate = float(framerate)
        self.height = height
        self.spritedown = Tkinter.PhotoImage(file='img/flappydown.gif')
        self.spriteup = Tkinter.PhotoImage(file='img/flappyup.gif')
        self.flapcount = 0
        self.bbox = None
        
        
    def flap(self):
        self.velocity = -(self.height / self.g) * 2
        self.flapcount = 5
        
        
    def logic(self):
        self.velocity += self.g / self.framerate
        self.y += self.velocity
        
        
    def render(self, canvas):
        self.logic()
        if self.flapcount > 0:
            sprite = canvas.create_image(self.x, self.y, image=self.spriteup)
            self.flapcount -= 1
        else:
            sprite = canvas.create_image(self.x, self.y, image=self.spritedown)
        self.bbox = canvas.bbox(sprite)

