# from turtle import Turtle, Screen
#
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()
#
# screen = Screen()
#
# # timmy_the_turtle.shape("turtle")
# # timmy_the_turtle.color("red")
#
# for _ in range(0,4):
#     tim.forward(100)
#     tim.right(90)
#
# screen.exitonclick()
import random

import heroes
import villains

from turtle import Turtle, Screen

# dash = Turtle()
# dash.shape("arrow")
#
#
# for _ in range(15):
#     dash.forward(10)
#     dash.penup()
#     dash.forward(10)
#     dash.pendown()

# bob = Turtle()
# screen = Screen()
colors  = ["red","green","blue","orange","purple","pink","yellow"]
#
# for seq in range(3, 10):
#     angle = int(360/seq)
#     for _ in range(seq):
#         bob.forward(50)
#         bob.right(angle)
#     color = random.choice(colors)
#     bob.color(color)
#
# screen.exitonclick()

bob = Turtle()
bob.speed('fastest')
# bob.pensize(10)
screen = Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = '#%02x%02x%02x' % (r,g,b)
    return rand_color

# turns = [0, 90, 180, 270]
# for _ in range(100):
#     bob.color(random_color())
#     direction = random.choice(turns)
#     bob.setheading(direction)
#     bob.forward(50)

for seq in range(360):
    bob.setheading(seq)
    if seq % 5 == 0:
        bob.color(random_color())
        bob.circle(100)

screen.exitonclick()