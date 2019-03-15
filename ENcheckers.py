from graphics import *

def draw_sqr (cX, cY, size, color, win):
    square = Rectangle(Point(cX, cY), Point(cX + size, cY + size))
    square.setFill(color_rgb(color,0 ,0 ))
    square.draw(win)


chSz = 50



chCol = 230

chwin = GraphWin("Checkers.py", chSz * 10, chSz * 10)
chwin.setCoords(0, 0, chSz * 10, chSz * 10)

for j in range (8):
    for i in range (8):
        if (j + i) % 2 == 0:
            chCol = 0
        else:
            chCol = 230
        draw_sqr((i + 1 ) * chSz, (j + 1) * chSz, chSz, chCol, chwin)
