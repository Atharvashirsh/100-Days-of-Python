from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.new_x = 10
        self.new_y = 10
        self.ball_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.new_x, self.ycor() + self.new_y)

    def bounce_y(self):
        self.new_y *= -1

    def bounce_x(self):
        self.new_x *= -1
        self.ball_speed *= 0.9

    def start_over(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.new_x *= -1
        self.new_y *= -1
