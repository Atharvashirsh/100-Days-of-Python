"""Basic functions"""

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()

"""Functions with parameters"""

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print("Isn't the weather nice today?")

# greet_with_name("Atharva")

"""Functions with more than one input"""

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# # greet_with("Atharva" , "Everywhere")
# greet_with("Everywhere" , "Atharva")


"""Functions with Keyword argument"""

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# # greet_with(name="Atharva", location="India")
# greet_with(location="India", name="Atharva" )


"""Area Calculation Exercise"""

# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height x wall width) ÷ coverage per can.


### CODE ###

# #Write your code below this line 👇
# import math

# def paint_calc(height, width, cover):
#     total_cans = math.ceil((height * width) / cover)

#     print(f"You'll need to buy {total_cans} of paint.")

# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


"""Prime number exercise"""

# Prime numbers are numbers that can only be cleanly divided by itself and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

### CODE ###
# #Write your code below this line 👇

# def prime_checker(number):
#     num = number // 2
#     isNotPrime = False
#     for i in range(2,num+1):
#         if number % i == 0:
#             isNotPrime = True
#             break
#     if isNotPrime:
#         print(f"{number} is not a prime number.")
#     else:
#         print(f"{number} is a prime number.")


# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

