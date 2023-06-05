import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Detect when the turtle player collides with a car and stop the game if this happens

# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase.
#  When the turtle hits a car, GAME OVER should be displayed in the centre

player = Player()
car_manager = CarManager()

screen.listen()

screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_all_cars()