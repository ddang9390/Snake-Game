from tkinter import Tk, BOTH, Canvas
from snake import Snake

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Snake Game")
        
        self.canvas = Canvas(self.root, background="black")
        self.canvas.pack()



    


