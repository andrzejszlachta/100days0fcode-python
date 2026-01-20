from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        pos = self.ycor()
        self.sety(pos + 20)

    def go_down(self):
        pos = self.ycor()
        self.sety(pos - 20)