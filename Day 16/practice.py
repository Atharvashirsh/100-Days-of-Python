# # import another_module

# # print(another_module.another_variable)

# from turtle import Turtle, Screen


# heisenberg = Turtle()
# print(heisenberg)
# heisenberg.shape("turtle")
# heisenberg.color("black", "green")
# heisenberg.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight, my_screen.canvwidth)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "r"
print(table)
