from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def l_scored(self):
        self.l_score += 1
        self.reset()
        self.update_scoreboard()

    def r_scored(self):
        self.r_score += 1
        self.rem
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"{self.l_score}     {self.r_score}",
            True,
            align="center",
            font=("Arial", 36, "normal"),
        )
