from tkinter import Tk,Label

class Snake:
    def __init__(self, canvas):
        self.body_size = 1
        self.body = canvas.create_rectangle(0, 0, 20, 20, fill="green")

        self.canvas = canvas

    
    def move(self, event):
        #Up
        if event.keycode == 38:
            x = 0
            y = -10
            self.canvas.move(self.body, x, y)
        
        #down
        if event.keycode == 40:
            x = 0
            y = 10
            self.canvas.move(self.body, x, y)

        #left
        if event.keycode == 37:
            x = -10
            y = 0
            self.canvas.move(self.body, x, y)

        #right
        if event.keycode == 39:
            x = 10
            y = 0
            self.canvas.move(self.body, x, y)