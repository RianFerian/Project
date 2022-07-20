from turtle import *
import colorsys

speed(300)
bgcolor("black")
pensize(4)
h = 0.0

for i in range(240):
    c = colorsys.rgb_to_hsv(h, 1, 1)
    color(c)
    h += 0.005
    for j in range(6):
        fd(i)
        rt(150)
        lt(60)
    rt(240)
done()

# Speed() -> speed of the turtle
# bgcolor() -> background colour
# fd() -> forward
# lt() -> left direction
# rt -> right direction