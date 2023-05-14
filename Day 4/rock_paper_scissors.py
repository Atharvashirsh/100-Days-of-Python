import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices = [rock, paper, scissors]

user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
user_choice = choices[user_number]

computer_choice = random.choice(choices)

print(user_choice)

print("Computer chose: ")

print(computer_choice)

if user_choice ==  computer_choice:
    print("Its a draw!")

elif user_choice == rock and computer_choice == paper:
    print("You Lose!")

elif user_choice == rock and computer_choice == scissors:
    print("You Win!") 

elif user_choice == paper and computer_choice == rock:
    print("You Win!")

elif user_choice == paper and computer_choice == scissors:
    print("You Lose!") 

elif user_choice == scissors and computer_choice == paper:
    print("You Win!")

elif user_choice == scissors and computer_choice == rock:
    print("You Lose!") 

