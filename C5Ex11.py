##Chapter 4 Exercise 11
##BLake Baker
from graphics import *


def main():
    win = GraphWin("5 Click House")
    win.setCoords(0, 0, 20.0, 20.0)

    print ("Please click two points for the box of the house")

    p1 = win.getMouse()
    p2 = win.getMouse()

    print(p1.getX(), p1.getY(), p2.getX(), p2.getY())

    vert1 = Line(p1,Point(p1.getX(), p2.getY()))                
    vert2 = Line(p2,Point(p2.getX(), p1.getY()))
    horiz1 = Line(p1,Point(p2.getX(), p1.getY()))                
    horiz2 = Line(p2,Point(p1.getX(), p2.getY()))

    vert1.draw(win)
    vert2.draw(win)
    horiz1.draw(win)
    horiz2.draw(win)

    p3 = win.getMouse()
    doorW = (p2.getX() - p1.getX())/5
    dP1 = Point(p3.getX() - (doorW/2), p3.getY())
    dP2 = Point(p3.getX() + (doorW/2), p3.getY())

    vertD1 = Line(Point(dP1.getX(),p1.getY()),Point(dP1.getX(),dP1.getY()))
    vertD2 = Line(Point(dP2.getX(),p1.getY()),Point(dP2.getX(),dP2.getY()))
    vertD1.draw(win)
    vertD2.draw(win)
    
    horizD = Line(dP1,dP2)
    horizD.draw(win)

    p4 = win.getMouse()
    wP1 = Point((p4.getX() - (doorW/4)),(p4.getY() - (doorW/4)))
    wP2 = Point((p4.getX() + (doorW/4)),(p4.getY() + (doorW/4)))
    w = Rectangle(wP1,wP2)
    w.draw(win)

    p5 = win.getMouse()

    roof = Polygon(Point(p1.getX(), p2.getY()),p2,p5)
    roof.draw(win)

main()

    

