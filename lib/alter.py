# STANDARD LIBRARY IMPORTS
import Tkinter as tk


class Alter:
    def __init__(self):
        self.g = None
        self.s = None


        self.master = tk.Tk()
        try:
            self.master.tk.call('wm', 'iconphoto', self.master._w,
                            tk.PhotoImage(file='img/icon.gif'))
        except:
            pass
        self.master.title('Altering Physics')

        # tumblers
        tk.Label(self.master, text='Mass of the Earth').pack()
        self.mass = tk.Scale(self.master, from_=40, to=360, orient=tk.HORIZONTAL)
        self.mass.pack()
        tk.Label(self.master, text='Height of the flight').pack()
        self.height = tk.Scale(self.master, from_=1, to=5, orient=tk.HORIZONTAL)
        self.height.pack()
        tk.Label(self.master, text='Horizontal speed').pack()
        self.speed = tk.Scale(self.master, from_=100, to=1000, orient=tk.HORIZONTAL)
        self.speed.pack()

        # submit button
        self.submit = tk.Button(self.master, text='Submit', command=self.calc)
        self.submit.pack()

        self.master.mainloop()


    def calc(self):
        self.g = float( self.mass.get() ) / self.height.get()**2
        self.s = self.speed.get()
        self.master.destroy()
