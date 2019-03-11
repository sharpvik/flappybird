import Tkinter


class Bird:
    def __init__(self, x, y, size, velocity, g, framerate, height):
        self.x = x
        self.y = y
        #self.size = size
        self.halfsize = size / 2
        self.velocity = float(velocity)
        self.g = g
        self.framerate = float(framerate)
        self.height = height
        self.spritedown = Tkinter.PhotoImage(file='img/flappydown.gif')
        self.spriteup = Tkinter.PhotoImage(file='img/flappyup.gif')
        
    def flap(self):
        self.velocity = float( -(self.height / self.g) ) * 2
        
    def logic(self):
        self.velocity += self.g / self.framerate
        self.y += self.velocity
        
    def render(self, canvas):
        self.logic()
        if self.velocity < 0:
            canvas.create_image(self.x, self.y, image=self.spriteup)
        else:
            canvas.create_image(self.x, self.y, image=self.spritedown)
