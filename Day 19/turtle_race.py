from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_color = screen.textinput(
    title="Make a bet", prompt="Which turtle will win the race? Enter a color: "
).lower()

is_race_on = True
colors = ["red", "yellow", "green", "blue", "purple", "pink"]
turtles = []

for turtle_index in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[turtle_index].penup()
    turtles[turtle_index].color(colors[turtle_index])
    turtles[turtle_index].goto(x=-230, y=-100 + 33 * turtle_index)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_color == winner:
                print(f"Congratulations!! The winner of the race was {winner} turtle")
            else:
                print(f"you lose! The winner of the race was {winner} turtle")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.bye()
