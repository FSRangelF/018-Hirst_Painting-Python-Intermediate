import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")

screen = t.Screen()
screen.exitonclick()

#challenge 1
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

#challenge 2
for i in range (15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

#challenge 3
sides = 3
while sides <= 10:
    angle = 360/sides
    for i in range (sides):
        timmy.color(random_color())
        timmy.forward(100)
        timmy.right(angle)


#challenge 4
timmy.speed("fastest")
timmy.widht(3)
while True:
    angle = 90*random.randint(0,3)
    for i in range (sides):
        timmy.color(random_color())
        timmy.right(angle)
        timmy.forward(10)
        

#challenge 4
timmy.widht(1)
steps = 36
angle = 360 / steps
for i in range (steps):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.tilt(angle)
        
