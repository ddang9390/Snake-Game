from tkinter import Tk, BOTH, Canvas
from snake import Snake

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Snake Game")
        
        self.__canvas = Canvas(self.__root, background="black")
        self.__canvas.pack()

        snake = Snake(self.__canvas)
        self.__root.bind("<Key>", snake.move)
        #self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.__root.mainloop()




