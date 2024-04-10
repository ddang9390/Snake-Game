from tkinter import Tk, BOTH, Canvas
from snake import Snake

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Snake Game")
        
        self.__canvas = Canvas(background="black")
        self.__canvas.pack()

        self.__root.bind("<Key>", Snake.move)
        #self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.mainloop()





