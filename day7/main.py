import random

from day7.hangman_art import hangman_pics, logo
from day7.hangman_dict import word_list

print(logo)


placeholder = ""
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

for letter in chosen_word:
    placeholder += "_"

while placeholder != chosen_word and lives > 0:
    guess = input("Guess a letter: ").lower()
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            placeholder_list = list(placeholder)
            placeholder_list[index] = letter
            placeholder = "".join(placeholder_list)
    if guess not in chosen_word:
        lives -= 1
        print("Lives left: ", lives)
    print(hangman_pics[6 - lives])
    print(placeholder)

if placeholder == chosen_word:
    print("You've won!")
else:
    print("You've lost!")