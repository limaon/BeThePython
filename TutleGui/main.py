import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(244, 245, 247), (235, 232, 226), (246, 238, 243), (232, 244, 240), (207, 156, 107), (60, 98, 131), (154, 82, 54), (140, 160, 189), (230, 203, 105), (160, 167, 41), (53, 174, 120), (125, 188, 172), (197, 138, 155), (66, 37, 31), (75, 113, 87), (127, 80, 90), (27, 46, 66), (183, 93, 110), (138, 28, 46), (199, 92, 73), (116, 36, 24), (57, 33, 46), (5, 66, 49), (80, 130, 192), (164, 189, 221), (35, 64, 101), (229, 205, 4), (20, 163, 169), (152, 211, 194), (221, 179, 171)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
