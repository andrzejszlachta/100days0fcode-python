import random
from turtle import Turtle, Screen

# class Racer:
#     def __init__(self, col, pos_x, pos_y):
#         racer = Turtle(shape='turtle')
#         racer.penup()
#         racer.color(col)
#         racer.goto(pos_x, pos_y)
#     def forward(self, distance):
#         self.forward(distance)

all_turtles = []

screen = Screen()

is_race_on = False

screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for index, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.speed("fastest")
    new_turtle.goto(-480, 300 - index * 100)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 450:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                print(f"You've lost. The {winning_color} is the winner.")

        rand_distance = random.randint(0,20)
        turtle.forward(rand_distance)

screen.exitonclick()