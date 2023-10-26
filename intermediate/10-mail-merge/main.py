# TODO: Create a letter using starting_letter.txt

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as basic_letter:
    starting_letter = basic_letter.read()

with open("./Input/Names/invited_names.txt") as names_to_insert:
    invited_names = names_to_insert.readlines()

for name in invited_names:
    stripped_name = name.strip()
    updated_letter = starting_letter.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt", "w") as final_letter:
        final_letter.write(updated_letter)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
