import turtle as t
import colorgram
import random

def random_color(color_list):
    color = random.choice(color_list).rgb
    return color

t.colormode(255)

screen = t.Screen()
#screen.screensize(canvheight=400)
#screen.screensize(canvwidth=800)
screen.title("Hirst Simulator")
screen.setup(width=1.0, height=1.0)
ytotal = screen.canvheight
xtotal = screen.canvwidth
startx = -(xtotal)
starty = -(ytotal)

image = '018-Hirst_Painting-Python-Intermediate\hirst.jpg'
number_of_colors = 30
color_list = colorgram.extract(image, number_of_colors)

# colors = []
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors.append((r,g,b))
# print(colors)

#color = [(248, 237, 218), (222, 155, 92), (214, 241, 229), (238, 206, 93), (106, 170, 201), (38, 109, 148), (202, 229, 239), (115, 192, 161), (151, 62, 94), (206, 80, 110), (244, 216, 227), (28, 133, 101), (203, 133, 155), (221, 82, 61), (181, 61, 45), (175, 165, 38), (140, 218, 197), (237, 162, 180), (40, 54, 112), (103, 41, 72), (138, 215, 228), (238, 169, 158), (16, 92, 69), (62, 164, 132), (28, 47, 87), (55, 156, 184), (72, 36, 64), (111, 116, 168), (16, 68, 50), (180, 186, 218)]

timmy = t.Turtle()
timmy.speed("fast")
timmy.hideturtle()
timmy.teleport(startx, starty)
for j in range (1, int(ytotal/50+2)):
    for i in range (1, int(xtotal/50+2)):
        timmy.pendown()
        timmy.dot(50, random_color(color_list))
        #timmy.dot(50,random.choice(color))
        timmy.penup()
        timmy.forward(100)

    timmy.backward(2*xtotal+100)
    timmy.left(90)
    timmy.forward(100)
    timmy.right(90)

screen.exitonclick()        
