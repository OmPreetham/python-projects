import random
import sys
from art import logo


def main():
    print(logo)

    low = 1
    high = 100
    while True:
        try:
            number = random.randint(low, high)
            user_response = input(
                f"Is {number} correct (C), or Too High (H), Too Low (L): "
            ).lower()
        except (ValueError, NameError):
            sys.exit("Don't cheat, give me correct response")
        else:
            if user_response == "h":
                high = number - 1
            elif user_response == "l":
                low = number + 1
            elif user_response == "c":
                print("Yeah, I guessed it...")
                return False
            else:
                print(
                    """
                      Enter correct response:
                      H for High
                      L for Low
                      C for Correct
                      """
                )


if __name__ == "__main__":
    main()
