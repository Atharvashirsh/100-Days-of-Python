"""Functions"""

# def my_function():
#     print("Hello")
#     print("Bye")

# my_function()

"""While Loop"""

# number = 20
# while number > 0:
#     print(number)
#     number -= 2


"""Hurdle 1"""

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for i in range(6):
#     jump()


"""Hurdle 2"""

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     jump()


"""Hurdle 3"""

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()


"""Hurdle 4"""

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def start_jump():
#     turn_left()
#     move()
    
# def across():
#     turn_right()
#     move()
#     turn_right()
#     move()
    
# while not at_goal():
#     if wall_in_front():
#         start_jump()
#         while wall_on_right():
#             move()
#         across()
#         while wall_on_right():
#             if front_is_clear():
#                 move()
#             else:
#                 turn_left()
#                 break
    
#     else:
#         move()
    