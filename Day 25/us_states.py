import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


writer = turtle.Turtle()

guess = screen.textinput(
    title="Guess the state", prompt="What's another state's name?"
).title()
# print(answer_state)

states = pandas.read_csv("50_states.csv")
# print(states["state"] == guess)

if guess in states["state"].to_list():
    data = list(states[states["state"] == guess])
    print(data)
    writer.penup()
    writer.hideturtle()
    print(data["state"], int(data["x"]), int(data["y"]))
    writer.goto(int(data.x), int(data.y))
    writer.write(data["state"], move=False, font=("Arial", 8, "normal"))


screen.exitonclick()
