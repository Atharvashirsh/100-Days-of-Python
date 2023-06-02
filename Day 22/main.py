from turtle import Screen, Turtle


def go_up():
    new_y = user_paddle.ycor() + 20
    user_paddle.goto(user_paddle.xcor(), new_y)


def go_down():
    new_y = user_paddle.ycor() - 20
    user_paddle.goto(user_paddle.xcor(), new_y)


def exit_game():
    global game_over
    game_over = True


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("My Pong Game.")

user_paddle = Turtle(shape="square")
user_paddle.penup()

user_paddle.shapesize(stretch_wid=5, stretch_len=1)
user_paddle.color("white")
user_paddle.goto(350, 0)
screen.update()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(exit_game, "X")

game_over = False

while not game_over:
    screen.update()

screen.exitonclick()
