import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()


guessed_states = []


states = pandas.read_csv("50_states.csv")

while len(guessed_states) < 50:
    guess = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    if guess == "Exit":
        break

    if guess in states["state"].to_list():
        guessed_states.append(guess)
        data = states[states["state"] == guess]
        writer.goto(int(data.x), int(data.y))
        writer.write(data["state"].item())

# states_to_learn.csv

states_to_learn = []
for state in states["state"].to_list():
    if state not in guessed_states:
        states_to_learn.append(state)

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
