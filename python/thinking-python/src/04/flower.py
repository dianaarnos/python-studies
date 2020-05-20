import turtle
from mypolygon import arc

def petal(turtle, length, angle):
    arc(turtle, length, angle)
    turtle.lt(180 - angle)
    arc(turtle, length, angle)

def flower(turtle, petals, length, angle):
    for i in range(petals):
        petal(turtle, length, angle)
        turtle.lt(360 / petals)

my_turtle = turtle.Turtle()

flower(my_turtle, 12, 100, 120)

turtle.mainloop()