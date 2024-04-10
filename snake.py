from tkinter import Tk,Label

class Snake:
    def __init__(self):
        pass

    
    def move(event):
        #Up
        if event.keycode == 38:
            print("up")
        
        #down
        if event.keycode == 40:
            print("down")

        #left
        if event.keycode == 37:
            print("left")

        #right
        if event.keycode == 39:
            print("right")