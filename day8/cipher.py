from day8 import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_input():
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
    if (direction != 'encode') and (direction != 'decode'):
        get_input()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    crypt(direction, text, shift)
    retry = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if retry == 'yes':
        get_input()
    elif retry == 'no':
        print("Goodbye!")
    else:
        print("Sorry, I didn't understand you.")

def crypt(direction, text, shift):
    output_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == 'decode':
                shift *= -1
            new_letter = alphabet[(index + shift)%len(alphabet)]
            output_text += new_letter
        else:
            output_text += letter
    print(f"Here's the {direction}d result: {output_text}!")

print(art.logo)
get_input()
