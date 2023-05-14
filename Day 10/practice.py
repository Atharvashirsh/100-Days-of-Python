# Functions with outputs


# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     return f"{formatted_f_name} {formatted_l_name}"


# formatted_name = format_name("aThArVa", "tiWArY")
# print(formatted_name)


# Functions with multiple return


# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs"

#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     return f"{formatted_f_name} {formatted_l_name}"


# formatted_name = format_name(
#     input("What is your first name? "), input("What is your last name? ")
# )
# print(formatted_name)


"""Days in Months Exercise"""

# In the starting code, you'll find the solution from the Leap Year challenge.
# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year."
# it should return True if it is a leap year and return False if it is not a leap year.

# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

# days_in_month(year=2022, month=2)

# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

# 28


### CODE ###


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]


# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


"""Docstrings"""

# def format_name(f_name, l_name):
#     """Takes first name and last name as inputs and convert them to
#     title case."""

#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs"

#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     return f"{formatted_f_name} {formatted_l_name}"

# format_name()
