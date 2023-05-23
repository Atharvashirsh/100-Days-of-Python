from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
    tim.forward(10)


screen = Screen()

screen.listen()
screen.onkey(fun=move_forwards, key="space")
screen.exitonclick()
