import random
import sys
from art import logo


def main():
    
    print(logo)

    number = random.randint(1, 100)
    while True:
        try:
            user_input = int(input("Enter a number to guess between 1-100: "))
        except ValueError:
            sys.exit("Enter Integer ")
        else:
            if user_input < number:
                print(f"Number Too Low, Enter Higher Number than {user_input}. ")
            elif user_input > number:
                print(f"Number Too High, Enter Lower Number than {user_input}. ")
            else:
                print(f"You guessed it right, {user_input} is the number. ")
                return False


if __name__ == "__main__":
    main()
