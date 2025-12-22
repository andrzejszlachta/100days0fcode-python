import random

from day7.hangman_art import hangman_pics, logo
from day7.hangman_dict import word_list

placeholder = ""
lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

for letter in chosen_word:
    placeholder += "_"

while placeholder != chosen_word and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in placeholder:
        print("You've already guessed a letter: ", guess)
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            placeholder_list = list(placeholder)
            placeholder_list[index] = letter
            placeholder = "".join(placeholder_list)
    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {guess}, that's not in the word.")
    print(hangman_pics[6 - lives])
    print(placeholder)
    print(f"******************** {lives}/6 LIVES Left ********************")

if placeholder == chosen_word:
    print(f"******************** YOU WIN! ********************")
else:
    print(f"******************** IT WAS {chosen_word}! YOU LOSE ********************")
