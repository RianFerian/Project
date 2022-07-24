from turtle import *
import turtle
turtle.bgcolor('black')
colors = ['red', 'dark red']
speed(1000)
for number in range(400):
    forward(number+1)
    right(89)
    pencolor(colors[number%2])
turtle.done()