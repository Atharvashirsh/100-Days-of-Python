import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase.
#  When the turtle hits a car, GAME OVER should be displayed in the centre

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_all_cars()

    # Collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20 and car.ycor() != player.ycor():
            game_is_on = False
            scoreboard.game_over()

    # Check if player crossed finished line
    if player.is_level_completed():
        scoreboard.level_up()
        player.goto_start()
        car_manager.level_up()

screen.exitonclick()
