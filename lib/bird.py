class Bird:
    def __init__(self, x, y, size, velocity, g):
        self.x = x
        self.y = y
        self.size = size
        self.halfsize = self.size // 2
        self.velocity = velocity
        self.g = g 
        
    def logic(self):
        self.velocity += self.g
        self.y += self.velocity
        
    def render(self, canvas):
        self.logic()
        canvas.create_rectangle(self.x - self.halfsize, self.y - self.halfsize,
                                self.x + self.halfsize, self.y + self.halfsize,
                                fill='yellow')