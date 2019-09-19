from graphics import *
def main():
	#x= top part of the window
	#y= left side of the window, y increase when going down

        #Window Name
	win=GraphWin("Traffic Light")
	#Horizontal Shape Traffic Light
	shape = Rectangle(Point(5,5),Point(80,40))
	shape . setOutline ("Black")
	shape . setFill ("White")
	#Red Circle
	shape.draw(win)
	shape=Circle(Point(23,23),9)
	shape.setOutline("Black")
	shape.setFill("Red")
	shape.draw(win)
	#Yellow Circle
	shape=Circle(Point(43,23),9)
	shape.setOutline("Black")
	shape.setFill("Yellow")
	shape.draw(win)
	#Green Circle
	shape=Circle(Point(63,23),9)
	shape.setOutline("Black")
	shape.setFill("Green")
	shape.draw(win)
	#Enter to quit so you can see the traffic light before it closes
	input("Press <Enter> to quit")
	win.close()
main()
