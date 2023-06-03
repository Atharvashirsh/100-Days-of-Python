from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def l_scored(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_scored(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(
            f"{self.l_score}", True, align="center", font=("Arial", 36, "normal")
        )
        self.goto(100, 220)
        self.write(
            f"{self.r_score}", True, align="center", font=("Arial", 36, "normal")
        )
