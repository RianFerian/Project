import turtle
import random

window = turtle.Screen()
arthur = turtle.Turtle()
window.colormode(255)
arthur.speed(0)
arthur.width(2)
window.bgcolor(0,0,0)
wht = 255
arthur.pencolor(255,255,wht)

def shape(angle,side,limit,wht):
    reverseDirection = 200
    arthur.forward(side)

    if side % (reverseDirection*2) == 0:
        angle = angle + 2
        wht = wht-10
        print(side)
    elif side % reverseDirection == 0 :
        angle = angle-2
        print(side)

    arthur.right(angle)
    side = side + 2
    if side < limit:
        shape(angle,side,limit,wht)
angle = 119
side = 0
limit = 600
shape(angle,side,limit,wht)

turtle.done()
