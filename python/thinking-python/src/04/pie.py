import turtle
from mypolygon import polygon

# TODO make it work with isosceles triangles instead of regular ones
# no need to import polygon

def triangle(turtle, side_length):
    polygon(turtle, side_length, 3)

def pie(turtle, side_length, pieces):
    for i in range(pieces):
        triangle(turtle, side_length)
        turtle.rt(360/pieces)

my_turtle = turtle.Turtle()

pie(my_turtle, 100, 6)

turtle.mainloop()