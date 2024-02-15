from turtle import Turtle
ALIGNMENT = "center"
FRONT = ("Arial", 22, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FRONT)
        self.hideturtle()

    def score_counter(self):
        self.score += 1
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FRONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FRONT)






