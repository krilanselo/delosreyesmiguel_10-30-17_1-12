import turtle
import math

def drawTriangle(myTurtle, q ,w, angle):
    r = math.sqrt(q*q + w*w - 2*q*w*math.cos(math.radians(angle)))
    alpha = math.degrees(math.asin(q / (r / math.sin(math.radians(angle)))))
    print(r)
    print(alpha)
    myTurtle.forward(q)
    myTurtle.right(180-angle)
    myTurtle.forward(w)
    myTurtle.right(180-alpha)
    myTurtle.forward(r)
    
wn = turtle.Screen()
t = turtle.Turtle()
drawTriangle(t, 100, 150, 40)
wn.exitonclick()
