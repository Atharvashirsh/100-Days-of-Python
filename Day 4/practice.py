"""Random Module"""

# import random

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float = random.random()
# print(random_float)


"""Heads or Tails exercise"""

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

### CODE ###

# #Write your code below this line 👇
# #Hint: Remember to import the random module first. 🎲

# import random

# coin = round(random.random())

# if coin == 1:
#     print("Heads")
# else:
#     print("Tails")

# ## 👆


"""Python Lists"""

# states_of_india = ["Haryana", "Maharashtra", "Bihar"]

# print(states_of_india)          # ['Haryana', 'Maharashtra', 'Bihar']

# print(states_of_india[0])       # Haryana
# print(states_of_india[1])       # Maharashtra
# print(states_of_india[2])       # Bihar

# print(states_of_india[-1])      # Bihar

# states_of_india[0] = "Jammu and Kashmir"
# print(states_of_india)           # ['Jammu and Kashmir', 'Maharashtra', 'Bihar']

# states_of_india.append("Punjab")
# print(states_of_india)          # ['Jammu and Kashmir', 'Maharashtra', 'Bihar', 'Punjab']

# states_of_india.extend(["Mizoram", "Meghalaya"])
# print(states_of_india)          # ['Jammu and Kashmir', 'Maharashtra', 'Bihar', 'Punjab', 'Mizoram', 'Meghalaya']


"""Who's Paying Exercise"""

# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

### CODE ###

# import random

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# pick = round(random.random() * len(names)) - 1
# print(f"{names[pick]} is going to pay!")

# ## 👆


"""Nested Lists"""

# dirty_dozen = ["strawberries", "celery", "apples", "cherries", "potato" ,"spinach"]
# print(dirty_dozen)

# fruits = ["strawberries", "apples", "cherries"]
# vegetables = ["celery", "potato", "spinach"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)


"""Treasure Island Exercise"""

# You are going to write a program which will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']


### CODE ###

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")