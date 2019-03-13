import Tkinter

class Obstacle:
    def __init__(self, x, y, height, framerate, speed):
        self.x = x
        self.y = y
        self.height = height
        self.ground = height / 10 * 8
        self.spriteheads = Tkinter.PhotoImage(file='img/obstacle.gif')
        self.spritecoline = Tkinter.PhotoImage(file='img/coline.gif')
        self.framerate = framerate
        self.speed = speed
        
    def logic(self):
        self.x -= self.speed / float(self.framerate)
        
    def render(self, canvas):
        # render the gates
        canvas.create_image(self.x, self.y, image=self.spriteheads)
        # render the lines
            # render up
        y = self.y - 123
        while y >= 0:
            canvas.create_image(self.x, y, image=self.spritecoline)
            y -= 3
            # render down
        y = self.y + 123
        while y <= self.ground:
            canvas.create_image(self.x, y, image=self.spritecoline)
            y += 3
        self.logic()
