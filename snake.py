from tkinter import Tk,Label

class Snake:
    def __init__(self, win, width, height):
        self.body_size = 1
        self.bodycoord = []
        self.body = []

        self.screen_width = width/2
        self.screen_height = height/2

        self.bodycoord.append([0, 0])
        self.bodycoord.append([0, 20])

        self.direction = "down"
        self.win = win

        self.alive = True

        for x, y in self.bodycoord:
            section = self.win.canvas.create_rectangle(x, y, x+20, y+20, fill="green")
            self.body.append(section)

    
    def change_direction(self, event):
        #Up
        if event.keycode == 38:
            self.direction = "up"
        
        #down
        if event.keycode == 40:
            self.direction = "down"

        #left
        if event.keycode == 37:
            self.direction = "left"

        #right
        if event.keycode == 39:
            self.direction = "right"

        
        self.constant_movement()

    def constant_movement(self):
        #Up
        if self.direction == "up":
            x = 0
            y = -10
        
        #down
        if self.direction == "down":
            x = 0
            y = 10

        #left
        if self.direction == "left":
            x = -10
            y = 0

        #right
        if self.direction == "right":
            x = 10
            y = 0


        for section in self.bodycoord:
            #cover section before moving
            self.win.canvas.create_rectangle(section[0], section[1], section[0] + 20, section[1] + 20, fill="black")

            section[0] += x
            section[1] += y

        self.draw_snake()

        if self.alive:
            self.win.root.after(50, self.constant_movement)

        self.check_collision()
  

    def check_collision(self):
        head = self.bodycoord[0]
        print(f"{head}, {self.direction}")

        #Up
        if self.direction == "up":
            if head[1] < 0:
                self.alive = False
        
        #down
        if self.direction == "down":
            if head[1] > self.screen_height:
                self.alive = False

        #left
        if self.direction == "left":
            if head[0] < 0:
                self.alive = False

        #right
        if self.direction == "right":
            if head[0] > self.screen_width:
                self.alive = False

        

    def draw_snake(self):
        self.body = []
        for section in self.bodycoord:
            self.body.append(self.win.canvas.create_rectangle(section[0], section[1], section[0] + 20, section[1] + 20, fill="green"))