import random
from game_data import data
import art
import os

# Clearing the screen
os.system("cls")

# Print logo
print(art.logo)


def generate_person():
    index = random.randint(0, len(data))

    person_name = data[index]["name"]
    followers = data[index]["follower_count"]
    details = data[index]["description"]
    country_name = data[index]["country"]

    print(f"Compare A : {a_person_name}, a {a_details}, from {a_country_name}")


def compare():
    {}


print(art.vs)

b_person_name = data[1]["name"]
b_followers = data[1]["follower_count"]
b_details = data[1]["description"]
b_country_name = data[1]["country"]

print(f"Against B : {b_person_name}, a {b_details}, from {b_country_name}")

print("Who has more followers? Type 'A' or 'B': ")
