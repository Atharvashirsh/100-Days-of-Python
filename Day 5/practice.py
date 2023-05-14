"""For loop with Lists"""

# fruits = ["Apple" , "Peach" , "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

"""Average Height Exercise"""


# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]


### CODE ###

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# sum = 0
# no_of_students = 0

# for num in student_heights:
#   sum += num

# for num in student_heights:
#   no_of_students += 1

# average = sum / no_of_students

# print(round(average))

# ### 👆


"""Highest Score Exercise"""

# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x



### CODE ###

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# biggest = student_scores[0]

# for i in student_scores:
#   if i > biggest:
#     biggest = i

# print(f"The highest score in class is {biggest}")
# ### 👆


"""For loop With Range"""

# for number in range(1,11):
#     print(number)

# for number in range(1,11,2):
#     print(number)

# total = 0
# for num in range(1,101):
#     total += num

# print(total)


"""Adding Evens Exercise"""

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100


### CODE ###

# #Write your code below this row 👇

# sum_of_even = 0

# for j in range(0,101):
#     if (j % 2 == 0):
#         sum_of_even += j

# print(sum_of_even)


# sum_of_even = 0

# for i in range(2,102,2):
#     sum_of_even += i

# print(sum_of_even)

# ### 👆


"""Fizz Buzz Exercise"""

# You are going to write a program that automatically prints the solution to the FizzBuzz game.

# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#   `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`


### CODE ###

# # Write your code below this row 👇

# for i in range(1, 101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

# ### 👆