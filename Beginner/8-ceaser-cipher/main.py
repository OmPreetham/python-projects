from art import logo
import sys

print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def ceaser(text, shift, direction):
    if direction == "encode" or direction == "decode":
        location = 0
        new_text = []

        for letter in text:
            if letter not in alphabet:
                new_text.append(letter)
            else:
                if direction == "encode":
                    location = alphabet.index(letter) + shift
                    if location > 24:
                        location = location - 26
                elif direction == "decode":
                    location = alphabet.index(letter) - shift
                    if location < 0:
                        location = location + 26
                cipher_letter = alphabet[location]
                new_text.append(cipher_letter)
        print(*new_text, sep="")
    else:
        sys.exit("Invalid direction, please type encode or decode. ")


end_loop = True
while end_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    yn = input("Type 'yes' to continue or type 'no' to exit. ")
    if yn == 'yes' or yn == 'y':
        end_loop = True
    elif yn == 'no' or yn == 'n':
        end_loop = False
    else:
        sys.exit("Invalid response, Please type 'yes' or 'no'.")
