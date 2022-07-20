from turtle import *
import colorsys

speed(0)
bgcolor('black')
pensize(2)
h=0.1

for i in range(160):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    circle(100,60-i)
    lt(i)
done()