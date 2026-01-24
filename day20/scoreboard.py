from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("best_score.txt") as file:
            self.best_score = int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.sety(250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} Best score: {self.best_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.best_score:
            self.best_score = self.score
            with open("best_score.txt", mode="w") as file:
                file.write(str(self.best_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('Game Over.', align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_score()