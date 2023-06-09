from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(30)


def move_backwards():
    tim.back(30)


def turn_clockwise():
    tim.right(15)


def turn_counter_clockwise():
    tim.left(15)


def clear():
    screen.reset()


screen.listen()


screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_counter_clockwise, key="a")
screen.onkey(fun=turn_clockwise, key="d")
screen.onkey(fun=clear, key="c")


screen.exitonclick()
