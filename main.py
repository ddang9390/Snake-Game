from graphics import Window
from snake import Snake

def main():
    screen_x = 800
    screen_y = 600

    win = Window(screen_x, screen_y)
    snake = Snake(win, screen_x, screen_y)
    win.root.bind("<Key>", snake.change_direction)

    
    win.root.after(50, snake.constant_movement)
    win.root.mainloop()

 


main()