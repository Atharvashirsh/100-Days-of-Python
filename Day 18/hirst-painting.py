# import colorgram

# colors = colorgram.extract("image.jpg", 38)

# turtle_colors = []

# for color in colors:
#     turtle_colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))

# print(turtle_colors)

import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

STARTING_X = 20 - screen.window_width() / 2
STARTING_Y = 20 - screen.window_height() / 2

print(STARTING_X, STARTING_Y)
turtle_colors = [
    (236, 244, 250),
    (236, 224, 80),
    (197, 7, 71),
    (195, 164, 13),
    (201, 75, 15),
    (231, 54, 132),
    (110, 179, 216),
    (217, 163, 101),
    (27, 105, 168),
    (35, 186, 109),
    (19, 29, 168),
    (13, 23, 66),
    (212, 135, 177),
    (233, 223, 7),
    (199, 33, 132),
    (13, 183, 212),
    (230, 166, 199),
    (126, 189, 162),
    (8, 49, 28),
    (40, 132, 77),
    (128, 219, 232),
    (58, 12, 25),
    (67, 22, 7),
    (114, 90, 210),
    (146, 216, 199),
    (179, 17, 8),
    (233, 66, 34),
    (11, 97, 52),
    (169, 181, 232),
    (241, 169, 155),
    (252, 7, 40),
    (10, 84, 100),
    (63, 98, 8),
    (14, 51, 250),
    (250, 11, 8),
]

t.colormode(255)

tim.hideturtle()
tim.speed(0)

tim.penup()
tim.goto(STARTING_X, STARTING_Y)

for i in range(1, 14):
    for j in range(16):
        tim.dot(20, random.choice(turtle_colors))
        tim.forward(50)
    tim.goto(STARTING_X, 20 - (screen.window_height() - i * 100) / 2)

screen.exitonclick()
