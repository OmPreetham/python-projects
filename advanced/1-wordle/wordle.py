# importing words.py to generate a random word for the game
from words import words
import random, sys
import json, os
from colorama import init
from termcolor import colored
from tabulate import tabulate

title = ["WORDLE"]

init()


# main function is where the code starts to executes at first
def main():
    # title of the game
    print("\nWELCOME TO ")
    print(tabulate(title, tablefmt="pretty"))
    # ask for player name
    player_name = players(input("ENTER YOUR USERNAME: ").strip())
    print(f"\nHey {player_name}!")
    while True:
        print(
            """
MENU:
1: PLAY
2: STATISTICS
3: PLAYER CHANGE
4: TUTORIAL
5: EXIT
            """
        )
        try:
            user_choice = int(input("CHOOSE AN OPTION FROM MENU: "))
        except ValueError:
            print("\nINVALID OPTION")
        else:
            # ask user to enter his choice from the menu items
            if user_choice == 1:
                player_tries = wordle(random_word_generator())
                data(player_name, player_tries)
            elif user_choice == 2:
                display_player_data(player_name)
            elif user_choice == 3:
                player_name = players(input("ENTER YOUR USERNAME: ").strip())
                print(f"\nHey {player_name}!")
            elif user_choice == 4:
                tutorial()
            elif user_choice == 5:
                print(tabulate(["THANKS-FOR-PLAYING"], tablefmt="grid"))
                sys.exit()
            else:
                print("\nINVALID OPTION")


def tutorial():
    print("\nWelcome to Worldle!")
    print(
        "Worldle is a word puzzle game where you need to guess a hidden five-letter word."
    )
    print("You have six attempts to guess the word.")
    print("After each guess, you will receive feedback:")
    print(
        "- Letters that are correct and in the right position will be marked in green."
    )
    print(
        "- Letters that are correct but in the wrong position will be marked in yellow."
    )
    print("- Letters that are incorrect will be marked in red.")
    print("Your goal is to guess the word within the given number of attempts.")
    print("Good luck!")


# funciton for storing player info
def players(player_name):
    return player_name


# function to generate random word form word list
def random_word_generator():
    word = random.choice(words())
    # the statement to neglect generating words with - as a separator
    while "-" in word or " " in word or len(word) != 5:
        word = random.choice(words())
    return word


# function to play game
def wordle(word):
    # variable to calculate the remaining tries
    lives = len(word) + 1
    tries = 1
    # to store word responses of the user typed words
    responses = []
    # store matched letter of a player word and word
    matched_letters = set()
    not_in_word = set()
    # loop runs until the user guesses the word or if the user is out of lives, which is 0
    while lives > 0:
        # stores all the individual matched locations of the user typed word
        matched_locations = []
        # print remaining lives
        print("\nYOU HAVE " + str(lives) + " TRIES")
        # print matched letters
        # print("MATCHED LETTERS:", " ".join(matched_letters))
        # print blocked letters
        # print("\nBLOCKED LETTERS:", " ".join(not_in_word))
        print("--------------------------------------")

        # stores player typed word
        player_word = (
            input(f"TO GUESS WORDLE, ENTER A {len(word)} LETTER WORD: ").strip().upper()
        )
        print()
        # if player word length is not equal to generated word
        if len(player_word) != len(word):
            print(f"\nENTER {len(word)} LETTER WORD")
        # if player word is not in word list
        elif player_word not in words():
            print("\nNOT IN WORD LIST")
        # if the player word is in word list
        else:
            # check if each letter in player word matches generated word if yes, store them or else append - to that location
            for word_letter, player_letter in zip(word, player_word):
                if player_letter in word:
                    matched_letters.add(player_letter)
                if player_letter not in word:
                    not_in_word.add(player_letter)
                # append the color according to the color of choice
                if word_letter == player_letter:
                    matched_locations.append(colored(player_letter, "green"))
                elif player_letter in word:
                    matched_locations.append(colored(player_letter, "yellow"))
                else:
                    matched_locations.append(colored(player_letter, "red"))

            # store the each response of the player word matched locaions
            responses.append(matched_locations)
            # print all responses of the player words
            print(tabulate(responses, tablefmt="heavy_grid"))
            # check if player word is word
            if word == player_word:
                # print the wordle
                print(tabulate([word], tablefmt="pretty"))
                print(
                    f"\n{random.choice(['MAGNIFICENT', 'SPLENDID', 'SUPER', 'HURRAY', 'YOU GOT THAT'])}"
                )
                return tries
            # if player word not equal to word decrement lives by 1
            else:
                lives -= 1
                tries += 1
                if lives == 0:
                    # print the wordle
                    print(tabulate([word], tablefmt="pretty"))
                    print("YOU LOST, BETTER LUCK NEXT TIME!")
                    return tries


# function for storing game data of each player
def data(player_name, player_tries):
    # initializing a empty dict
    player_dict = {}

    # create folder name player_info if folder doesn't exist
    if not os.path.exists("player_info"):
        os.makedirs("player_info")

    # Construct the full path to the JSON file
    file_path = os.path.join("player_info", player_name + ".json")

    # Load existing data or initialize player_dict if the JSON file doesn't exist
    try:
        with open(file_path, "r") as userfile:
            player_dict = json.load(userfile)
    except FileNotFoundError:
        # add name of the player
        player_dict = {"name": player_name}
        # matches played
        player_dict = {"matches": 0}
        # matches won
        player_dict = {"win": 0}
        # matches loss
        player_dict = {"loss": 0}
        # match streak
        player_dict = {"max_streak": 0}

    # add name of the player
    player_dict["name"] = player_name
    # increment matches played by 1
    player_dict["matches"] = player_dict.get("matches", 0) + 1
    # create guesses distrubution variable for the first time
    if player_dict["matches"] == 1:
        for _ in range(7):
            if _ > 0:
                player_dict[f"{_}_try"] = 0
    # matches loss and win
    if player_tries == 7:
        player_dict["loss"] = player_dict.get("loss", 0) + 1
        player_dict["current_streak"] = 0
    else:
        player_dict["win"] = player_dict.get("win", 0) + 1
        player_dict[f"{player_tries}_try"] = (
            player_dict.get(f"{player_tries}_try", 0) + 1
        )
        player_dict["current_streak"] = player_dict.get("current_streak", 0) + 1
        # assign current_streak to max_streak if the player wins their first match
        if player_dict["win"] == 1:
            player_dict["max_streak"] = player_dict["current_streak"]
        # increment max streak if the current streak is greater then max streak
        elif player_dict["current_streak"] > player_dict["max_streak"]:
            player_dict["max_streak"] = player_dict.get("max_streak", 0) + 1

    # calculate win and loss percentage
    player_dict["win_percent"] = (
        player_dict.get("win", 0) / player_dict["matches"]
    ) * 100
    player_dict["loss_percent"] = (
        player_dict.get("loss", 0) / player_dict["matches"]
    ) * 100

    # Save the updated player_dict to the JSON file
    with open(file_path, "w") as userfile:
        json.dump(player_dict, userfile)


# function to display player data
def display_player_data(player_name):
    # Construct the full path to the JSON file
    file_path = os.path.join("player_info", player_name + ".json")
    # Load existing data or initialize player_dict if the JSON file doesn't exist
    try:
        # print the user data
        with open(file_path) as userfile:
            info = json.load(userfile)
    except FileNotFoundError:
        print(
            "\nUSERNAME NOT FOUND IN DATABASE. I ASSUME, YOU HAVEN'T PLAYED A SINGLE MATCH. "
        )
    else:
        print("\nSTATISTICS: \n")
        table = [
            [
                info["name"],
                info["matches"],
                info["win_percent"],
                info["current_streak"],
                info["max_streak"],
            ]
        ]
        table_headers = [
            "USERNAME",
            "PLAYED",
            "WIN %",
            "CURRENT STREAK",
            "MAX STREAK",
        ]
        print(tabulate(table, headers=table_headers, tablefmt="heavy_grid"))
        print("\nGUESS DISTRIBUTION: \n")
        print("1: " + "-" * info["1_try"], str(info["1_try"]))
        print("2: " + "-" * info["2_try"], str(info["2_try"]))
        print("3: " + "-" * info["3_try"], str(info["3_try"]))
        print("4: " + "-" * info["4_try"], str(info["4_try"]))
        print("5: " + "-" * info["5_try"], str(info["5_try"]))
        print("6: " + "-" * info["6_try"], str(info["6_try"]))


# run the program when the main is called by function itself
if __name__ == "__main__":
    main()
