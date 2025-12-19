import random
import sys

pictures = ['''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
choices = ["rock", "paper", "scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if not (0 > user_choice > 2):
    print("Invalid number!")
    sys.exit()

computer_choice = random.randint(0,2)

# user choice
print("You chose: ", choices[user_choice])
print(pictures[user_choice])

# computer choice
print("Computer chose: ", choices[computer_choice])
print(pictures[computer_choice])

# result
if user_choice == computer_choice:
    print("It's a tie!")
elif ((user_choice == 0 and computer_choice == 2) or
      (user_choice == 1 and computer_choice == 0) or
      (user_choice == 2 and computer_choice == 1)):
    print("You won!")
else:
    print("You lost!")