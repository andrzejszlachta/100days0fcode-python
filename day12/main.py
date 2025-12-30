import random
import art

DIFFICULTIES = {"easy": 10, "hard": 5}

def init():
    def decrease_lives(count):
        count -= 1
        if count > 0:
            print("Guess again.")
        return count

    number = random.randint(1, 100)

    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    lives = DIFFICULTIES[difficulty]
    correct_answer = False

    while (lives > 0) and not correct_answer:
        print("You have " + str(lives) + " attempts remaining to guess the number.")
        user_answer = int(input("Make a guess: "))

        if user_answer == number:
            print(f"You got it! The number was {number}.")
            correct_answer = True
        elif user_answer < number:
            print("Too low.")
        elif user_answer > number:
            print("Too high.")
        lives = decrease_lives(lives)

    if lives == 0:
        print("You've run out of guesses, you lose.")

init()
