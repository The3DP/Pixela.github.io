##
# 2D Animations
##

import turtle, colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

for i in range(360):
    color = colorsys.hsv_to_rgb(i/360, 1.0, 1.0)
    t.color(color)
    t.circle(i)
    t.right(59)
