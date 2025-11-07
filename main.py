import turtle as t
import colorgram
import random

def random_color(color_list):
    color = random.choice(color_list).rgb
    return color

t.colormode(255)

screen = t.Screen()
screen.screensize(canvheight=400)
screen.screensize(canvwidth=800)
screen.title("Hirst Simulator")
screen.setup(width=1.0, height=1.0)
ytotal = screen.canvheight
xtotal = screen.canvwidth
startx = -(xtotal)
starty = -(ytotal)

image = '018-Hirst_Painting-Python-Intermediate\hirst.jpg'
number_of_colors = 10
color_list = colorgram.extract(image, number_of_colors)

timmy = t.Turtle()
timmy.speed("fast")
timmy.hideturtle()
timmy.teleport(startx, starty)
for j in range (1, int(ytotal/50+2)):
    for i in range (1, int(xtotal/50+2)):
        timmy.pendown()
        timmy.dot(50, random_color(color_list))
        timmy.penup()
        timmy.forward(100)

    timmy.backward(2*xtotal+100)
    timmy.left(90)
    timmy.forward(100)
    timmy.right(90)

screen.exitonclick()        
