import random
from game_data import data
import art
import os


def compare(num1, num2):
    if num1 >= num2:
        return True
    else:
        return False


def random_num():
    return random.randint(0, len(data))


def get_followers(index):
    return data[index]["follower_count"]


def generate_person(index):
    person_name = data[index]["name"]
    details = data[index]["description"]
    country_name = data[index]["country"]

    return f"{person_name}, a {details}, from {country_name}"


def higherlower():
    should_continue = True
    score = 0

    val1 = random_num()
    print(str(val1) + "\n")
    while should_continue:
        a_followers = get_followers(val1)
        print("Compare A: " + generate_person(val1))

        print(art.vs)

        val2 = random_num()
        print(str(val2) + "\n")
        b_followers = get_followers(val2)
        print("Against B: " + generate_person(val2))

        pick = input("Who has more followers? Type 'A' or 'B': ").lower()

        if pick == "a":
            should_continue = compare(a_followers, b_followers)
            if not should_continue:
                print(f"You lose! Your score was {score}")
            else:
                score += 1

                # Clear screen
                os.system("cls")

                # Print logo
                print(art.logo)

                print(f"You are correct! Your score is {score}")

        elif pick == "b":
            should_continue = compare(b_followers, a_followers)
            if not should_continue:
                print(f"You lose! Your score was {score}")
            else:
                score += 1
                val1 = val2

                # Clear screen
                os.system("cls")

                # Print logo
                print(art.logo)

                print(f"You are correct! Your score is {score}")

        else:
            print("Invalid value selected")
            should_continue = False


# Clear screen
os.system("cls")

# Print logo
print(art.logo)

higherlower()
