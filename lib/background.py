class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def render(self, canvas):
        canvas.create_rectangle(0, 0, self.width, self.height,
                                fill='#54c0ca', outline='')