"""Data types"""
# type(x) : This function gives the datatype of 'x'


"""String"""

# a = "Atharva"
# print(a)          # Atharva
# print(type(a))    # <class 'str'>
# print(a[0])       # A
# print(a[6])       # a

"""Integer"""

# n = 12345
# print(type(n))    # <class 'int'>
# print(123 + 345)  # 468
# print(123_345)    # 123345 (Python interprets 1_2 as 12, underscores are just an equivalent of commas when writing large numbers)

"""Float"""

# pi = 3.14159
# print(pi)         # 3.14159
# print(type(pi))   # <class 'float'>

"""Boolean"""

# x = True
# print(type(x))    # <class 'bool'>
# print(x)          # True

###############################################################

"""Type Error"""

# print("a " + 3 + " c")      # TypeError: can only concatenate str (not "int") to str
# print(len(35))              # TypeError: object of type 'int' has no len()

"""Type Checking"""

# print(type("abc"))        # <class 'str'>
# print(type(123))          # <class 'int'>
# print(type(3.14))         # <class 'float'>
# print(type(True))         # <class 'bool'>

"""Type Conversion"""

# number = 12345
# print(type(number))  # <class 'int'>

# number = str(number)
# print(type(number))  # <class 'str'>

# number = float(number)
# print(type(number))  # <class 'float'>

"""Datatypes exercise"""
#
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# # Write your code below this line 👇

# ## Answer 🔽

# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])
# print(num1 + num2)

# ## 🔼

###############################################################

"""Mathematical Operations"""

# print(2 + 5)  # Addition -> 7
# print(5 - 3)  # Subtraction -> 2
# print(3 * 6)  # Multiplication -> 18
# print(16 / 4)  # Division -> 4.0 (always float)
# print(18 // 4)  # Floor division -> 4
# print(18 % 4)  # Modulus division -> 2
# print(4**3)  # Exponential -> 64

"""Operators priority"""

# PEMDAS
# Parenthesis ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

###############################################################

"""BMI Calculator Exercise"""

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# bmi = int(weight) / float(height) ** 2
# print(int(bmi))

# ## 👆

###############################################################

"""Number Manipulation"""

# sum += 1          # sum = sum + 1
# sum -= 1          # sum = sum - 1
# sum *= 1          # sum = sum * 1
# sum /= 1          # sum = sum / 1
# sum **= 3         # sum = sum**3

"""f-Strings"""

# score = 98
# height = 1.7
# isWinning = True

# print(
#     f"Your score is {score}, your height is {height} and you are winning is {isWinning}"
# )

# Your score is 98, your height is 1.7 and you are winning is True

###############################################################

"""Life in weeks Exercise"""

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
## 👆