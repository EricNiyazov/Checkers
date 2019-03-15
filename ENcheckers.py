from graphics import *

def draw_sqr (cX, cY, size, win):
    square = Rectangle(Point(cX, cY), Point(cX + size, cY + size))
    square.setFill(color_rgb(230,0 ,0 ))
    square.draw(win)


chwin = GraphWin("Checkers.py", 500, 500)
chSz = 50
chCol = 230

for j in range (8):
    for i in range(8):
        draw_sqr((i + 1 ) * chSz, (j + 1) * chSz, chSz, chwin)
