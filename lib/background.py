class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        
    def render(self, canvas):
        canvas.create_rectangle(0, 0, self.width + 50, self.height + 50,
                                fill='#54c0ca', outline='')