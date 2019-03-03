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
        
    def flap(self):
        self.velocity = float( -(self.height / self.g) ) * 2
        
    def logic(self):
        self.velocity += self.g / self.framerate
        self.y += self.velocity
        
    def render(self, canvas):
        self.logic()
        canvas.create_oval(self.x - self.halfsize, self.y - self.halfsize,
                           self.x + self.halfsize + 7, self.y + self.halfsize,
                           fill='#830f72', outline='#523746', width=3)