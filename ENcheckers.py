from graphics import *

def draw_sqr (cX, cY, size, win):
    square = Rectangle(Point(cX, cY), Point(cX + size, cY + size))
    square.setFill(color_rgb(230,0 ,0 ))
    square.draw(win)


chwin = GraphWin("Checkers.py", 500, 500)


draw_sqr (0,0,50,chwin)
