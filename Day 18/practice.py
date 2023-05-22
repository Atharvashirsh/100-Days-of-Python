import turtle as t
import random

tim = t.Turtle()
# tim.shape("turtle")
tim.color("black", "green")


"""Challenge 1 - Draw a square"""

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


"""Challenge 2 - Draw a dashed line"""

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


"""Challenge 3 - Draw shapes"""

# colors = [
#     "blue",
#     "light blue",
#     "sea green",
#     "lime",
#     "yellow",
#     "dark orange",
#     "orange",
#     "magenta",
#     "indigo",
#     "dark slate blue",
#     "deep pink",
#     "hot pink",
# ]

# num_of_sides = 3
# for _ in range(8):
#     tim.color(random.choice(colors))
#     angle = 360 / num_of_sides
#     for i in range(num_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#     num_of_sides += 1


"""Challenge 4 - Generate a random walk"""

# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# directions = [0, 90, 180, 270]
# tim.speed(0)
# tim.width(15)

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


"""Challenge 5 - Draw a spirograph"""
tim.speed(0)
angle = 10
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


while angle <= 360:
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(angle)
    angle += 10

screen = t.Screen()
screen.exitonclick()
