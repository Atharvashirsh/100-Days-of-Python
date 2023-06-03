from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game.")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_over = False

while not game_over:
    ball.move()
    screen.update()
    time.sleep(ball.ball_speed)

    # Detect collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect r_paddle miss
    if ball.xcor() > 400:
        score.l_scored()
        ball.start_over()

    # Detect l_paddle miss
    if ball.xcor() < -400:
        score.r_scored()
        ball.start_over()

screen.exitonclick()
