import Tkinter

class Obstacle:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.spritehead = Tkinter.PhotoImage(file='img/colhead.gif')
        self.spritecoline = Tkinter.PhotoImage(file='img/coline.gif')
        
    def logic(self):
        pass
        
    def render(self, canvas):
        canvas.create_image(self.x, self.y, image=self.spritehead)
        canvas.create_image(self.x, self.y + 19, image=self.spritecoline)
