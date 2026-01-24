with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()
    for name in invited_names:
        stripped_name = (name[0:-2])
        new_letter = letter.replace("[name]", stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
