from turtle import Turtle

PRIMARY_FONT = ("Courier", 24, "normal")
SECONDARY_FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level : {self.level}", move=False, font=PRIMARY_FONT)

    def level_up(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER.", move=False, font=PRIMARY_FONT)
        self.goto(-150, -50)
        self.write("Click anywhere to exit.", move=False, font=SECONDARY_FONT)
