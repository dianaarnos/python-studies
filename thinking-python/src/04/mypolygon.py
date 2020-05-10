import turtle
import math

def polygon(turtle, length, sides):
    for i in range(sides):
        turtle.fd(length)
        turtle.lt(360 / sides)

def square(turtle, side_length):
    polygon(turtle, side_length, 4)
 
def arc(turtle, radius, angle):
    arc_length = angle * 2 * math.pi * radius / 360
    
    steps = arc_length / 4
    step_length = arc_length / steps
    step_angle = angle / steps

    for i in range (int(steps)):
        turtle.lt(step_angle)
        turtle.fd(step_length)

def circle(turtle, radius):
    arc(turtle, radius, 360)



bob = turtle.Turtle()

# square(bob, 100)

# polygon(bob, 100, 10)

# circle(bob, 100)

arc(bob, 100, 90)

turtle.mainloop()