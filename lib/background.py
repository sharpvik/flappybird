class Background:
    def __init__(self, width, height, speed, framerate):
        self.width = width
        self.height = height
        self.ground = height / 10 * 8
        self.speed = speed
        self.x = 0
        self.framerate = float(framerate)
        
    def logic(self):
        self.x -= self.speed / self.framerate
        if self.x <= -360:
            self.x = 0
        
    def render(self, canvas):
        # sky
        canvas.create_rectangle(0, 0, self.width, self.ground,
                                fill='#54c0ca', outline='')
        # ground
        canvas.create_rectangle(0, self.ground, self.width, 
                                self.height, fill='#dfd798', outline='')
        # ground border
        canvas.create_rectangle(0, self.ground, self.width,
                                self.ground + 3, 
                                fill='#543847', outline='')
        canvas.create_rectangle(0, self.ground + 3, self.width,
                                self.ground + 21, 
                                fill='#9ee460', outline='')
        canvas.create_rectangle(0, self.ground + 21, self.width,
                                self.ground + 24, 
                                fill='#567e28', outline='')
        canvas.create_rectangle(0, self.ground + 24, self.width,
                                self.ground + 27, 
                                fill='#d6a755', outline='')
        # squares
        self.logic()
        x = self.x + 0
        while x < self.width + 20:
            canvas.create_rectangle(x, self.ground + 3, x + 90, self.ground + 21,
                                    fill='#76bd3b', outline='')
            x += 180