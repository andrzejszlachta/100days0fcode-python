from turtle import Turtle, Screen

import random
import colorgram

raw_colors = colorgram.extract('image.jpg', 30)

colors = []
for color in raw_colors:
    colors.append('#%02x%02x%02x' % (color.rgb.r, color.rgb.b, color.rgb.b))

dot = Turtle()
dot.speed("fastest")
dot.penup()
dot.hideturtle()

screen = Screen()

INIT_POS = (-380, -380)
SPACE = 80
DOT_SIZE = 50
NUMBER_OF_DOTS = 100

dot.setx(INIT_POS[0])
dot.sety(INIT_POS[1])

def print_dot():
    dot.pendown()
    dot.dot(DOT_SIZE, random.choice(colors))
    dot.penup()

for index in range(NUMBER_OF_DOTS):
    dot.setx(INIT_POS[0] + (SPACE * (index % 10)))
    dot.sety(INIT_POS[1] + (SPACE * (int(index / 10))))
    print_dot()

screen.exitonclick()