import wordle
from words import words
import pytest, os
from colorama import init
from termcolor import colored


def main():
    init()
    pass


def test_players():
    assert wordle.players("OmPreetham") == "OmPreetham"


def test_data():
    player_name = "O"
    player_tries = 1
    player_dict = {}

    # create folder name player_info if folder doesn't exist
    if not os.path.exists("player_info"):
        os.makedirs("player_info")

    # Construct the full path to the JSON file
    file_path = os.path.join("player_info", player_name + ".json")

    assert file_path == "player_info/O.json"

    # add name of the player
    player_dict["name"] = player_name
    # increment matches played by 1
    player_dict["matches"] = player_dict.get("matches", 0) + 1

    assert player_dict == {"matches": 1, "name": "O"}

    # create guesses distrubution variable for the first time
    if player_dict["matches"] == 1:
        for _ in range(7):
            if _ > 0:
                player_dict[f"{_}_try"] = 0

    assert player_dict == {
        "1_try": 0,
        "2_try": 0,
        "3_try": 0,
        "4_try": 0,
        "5_try": 0,
        "6_try": 0,
        "name": "O",
        "matches": 1,
    }

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

    assert player_dict == {
        "name": "O",
        "matches": 1,
        "1_try": 1,
        "2_try": 0,
        "3_try": 0,
        "4_try": 0,
        "5_try": 0,
        "6_try": 0,
        "win": 1,
        "current_streak": 1,
        "max_streak": 1,
    }

    # calculate win and loss percentage
    player_dict["win_percent"] = (
        player_dict.get("win", 0) / player_dict["matches"]
    ) * 100
    player_dict["loss_percent"] = (
        player_dict.get("loss", 0) / player_dict["matches"]
    ) * 100

    assert player_dict == {
        "name": "O",
        "matches": 1,
        "1_try": 1,
        "2_try": 0,
        "3_try": 0,
        "4_try": 0,
        "5_try": 0,
        "6_try": 0,
        "win": 1,
        "current_streak": 1,
        "max_streak": 1,
        "win_percent": 100.0,
        "loss_percent": 0.0,
    }


def test_wordle():
    word = "GABBY"

    lives = len(word) + 1

    assert lives == 6

    matched_letters = set()
    not_in_word = set()
    matched_locations = []

    player_word = "GABBY"
    if player_word != word:
        # if player word length is not equal to generated word
        assert len("MOTHER") != len(word)

        # if player word is not in word list
        assert "KILO" not in words()

        # check if each letter in player word matches generated word if yes, store them or else append - to that location
    else:
        for word_letter, player_letter in zip(word, player_word):
            if player_letter in word:
                matched_letters.add(player_letter)
            if player_letter not in word:
                not_in_word.add(player_letter)
            if word_letter == player_letter:
                matched_locations.append(colored(player_letter, "green"))
            elif player_letter in word:
                matched_locations.append(colored(player_letter, "yellow"))
            else:
                matched_locations.append(colored(player_letter, "red"))

        assert matched_letters == {"A", "B", "G", "Y"}

        assert matched_locations == [
            "\x1b[32mG\x1b[0m",
            "\x1b[32mA\x1b[0m",
            "\x1b[32mB\x1b[0m",
            "\x1b[32mB\x1b[0m",
            "\x1b[32mY\x1b[0m",
        ]

        assert not_in_word == set()

        # check if player word is word
        assert word == player_word


if __name__ == "__main__":
    main()
