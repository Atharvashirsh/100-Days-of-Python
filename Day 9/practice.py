"""Dictionaries"""

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# # Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# # Add items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# Create an empty dictionary
# useless_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary["Bug"])

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


"""Grading program exercise"""

# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain
# student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

# DO NOT modify lines 1-7 to change the existing student_scores dictionary.

# DO NOT write any print statements.

# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"


### CODE ###

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     marks = student_scores[key]
#     grade = ""
#     if marks > 90:
#         grade = "Outstanding"
#     elif marks > 80:
#         grade = "Exceeds Expectations"
#     elif marks > 70:
#         grade = "Acceptable"
#     else:
#         grade = "Fail"

#     student_grades[key] = grade

# # 🚨 Don't change the code below 👇
# print(student_grades)


"""Nesting"""

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# # Nesting a list in dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# # Nesting a dictionary in dictionary

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 4,
#     },
# }

# # Nesting a dictionary in list

# travel_log = [
#     {
#         "country_visited": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     {
#         "country_visited": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 4,
#     },
# ]


"""Dictionary in List exercise"""

# You are going to write a program that adds to a travel_log.
# You can see a travel_log which is a List that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line 21
#  to add the entry for Russia to the travel_log.

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# You've visited Russia 2 times.

# You've been to Moscow and Saint Petersburg.


### CODE ###

travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country, visits, cities_visited):
    travel_details = {}

    travel_details["country"] = country
    travel_details["visits"] = visits
    travel_details["cities"] = cities_visited

    travel_log.append(travel_details)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("India", 100, ["Delhi", "Ladakh"])
print(travel_log)
