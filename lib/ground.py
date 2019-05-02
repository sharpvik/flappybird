class Ground:
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


    def check_collision(self, bbox):
        return self.ground < bbox[3]
        

    def render(self, canvas):
        # ground
        canvas.create_rectangle(-50, self.ground, self.width + 50, 
                                self.height + 50, fill='#dfd798', outline='')
        # ground border
        canvas.create_rectangle(0, self.ground, self.width + 50,
                                self.ground + 3, 
                                fill='#543847', outline='')
        canvas.create_rectangle(0, self.ground + 3, self.width + 50,
                                self.ground + 21, 
                                fill='#9ee460', outline='')
        canvas.create_rectangle(0, self.ground + 21, self.width + 50,
                                self.ground + 24, 
                                fill='#567e28', outline='')
        canvas.create_rectangle(0, self.ground + 24, self.width + 50,
                                self.ground + 27, 
                                fill='#d6a755', outline='')
        # squares
        self.logic()
        x = self.x + 0
        while x < self.width + 20:
            canvas.create_rectangle(x, self.ground + 3, x + 90, self.ground + 21,
                                    fill='#76bd3b', outline='')
            x += 180
