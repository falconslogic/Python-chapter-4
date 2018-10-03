##Chapter 4 Exercise 2
##BLake Baker

from graphics import *
##
##I wanted the target to look accurate.
##
def main():
    win = GraphWin("Target")
    win.setCoords(0.0, 0.0, 20.0, 20.0)

    p1 = Point(10,10)
    
    redTarget = Circle(p1,3)
    redTarget.setFill("red")
    
    blueTarget = Circle(p1,5)
    blueTarget.setFill("blue")
    
    blackTarget = Circle(p1,7.5)
    blackTarget.setFill("black")
    
    whiteTarget = Circle(p1,9)
    whiteTarget.setFill("white")

    yellowTarget = Circle(p1,1.5)
    yellowTarget.setFill("yellow")      

    whiteTarget.draw(win)
    blackTarget.draw(win)
    blueTarget.draw(win)
    redTarget.draw(win)
    yellowTarget.draw(win)


main()

    

