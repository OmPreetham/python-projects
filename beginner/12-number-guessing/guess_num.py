import guess_num_computer, guess_num_user
import sys


def main():
    while True:
        print("Welcome to Number Guessing Game: ")
        print(
            """
            Menu:
            1: Computer Guesses Your Number
            2: I Guess Computer Generated Number
            3: Exit
            """
        )
        try:
            user_choice = int(input("Choose an Option from the Menu: "))
        except ValueError:
            print(
                    """
                    Choose a right option.
                    1 to 'Computer Guesses Your Number'
                    2 to 'I Guess Computer Generated Number'
                    3 to 'Exit'
                    """
                )
        else:
            if user_choice == 1:
                guess_num_computer.main()
            elif user_choice == 2:
                guess_num_user.main()
            elif user_choice == 3:
                sys.exit()
            else:
                print(
                    """
                    Choose a right option.
                    1 to 'Computer Guesses Your Number'
                    2 to 'I Guess Computer Generated Number'
                    3 to 'Exit'
                    """
                )


if __name__ == "__main__":
    main()
