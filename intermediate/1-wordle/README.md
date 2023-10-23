# Wordle in Command Line Interface
## Video Demo:  <URL HERE>
## Requirements:

The game was created with the assistance of some open source libraries: **random, sys, os, json, tabulate, colorama, and termcolor**. It also includes two important files: **words.py** and **wordle.py**

### requirements.txt

To install all the libraries or modules this project uses and to make it run smoothly, run the **requirements.txt** file. The file is located in the root folder.

**How to install requirements.txt:**

- install python
- install pip
- then run `pip install -r requirements.txt` from the project root folder in CLI.

## Description:

**Welcome to Worldle!**

- Worldle is a word puzzle game where you need to guess a hidden five-letter word.
- You have six attempts to guess the word.
- After each guess, you will receive feedback:
    - Letters that are correct and in the right position will be marked in green.
    - Letters that are correct but in the wrong position will be marked in yellow.
    - Letters that are incorrect will be marked in red.
- Your goal is to guess the word within the given number of attempts.
- Good luck!

### words.py

**words.py** contains a **words()** function that holds a list of English words. This file was created for the purpose of importing all the words into **wordle.py** in order to generate a random 5-letter word.

### wordle.py

**wordle.py** comprises seven functions: **main(),players(), random_word_generator(), wordle(), data(), display_player_data(), and tutorial()**

- The **main()** function serves as an entry point to access all the other functions and provides the user with input choices from a menu.

- The **players()** function prompts the user to enter their username and returns it.

- The **random_word_generator()** function generates a random 5-letter word from "words.py" and returns it.

- The **wordle()** function is where all the calculations take place. This includes checking if the user's input is a five-letter word, verifying if the input is in the word list, checking if the user's input matches the randomly generated word, and if the user's input is in the word list and is a five-letter word but not the random generated word, then it checks the positions of each letter with the random generated word and assigns a color to them with the help of colorama module. The user starts with 6 lives (5 words + 1), and a life is deducted each time the user fails until it reaches zero. All user responses are stored in a responses list and displayed on the screen every time the user's input word is in the word list. The function returns the number of tries for calculating the user's performance compared to other users. Finally, if the user correctly identifies the word or has exhausted all their tries/lives, the randomly generated word is displayed.

- The **data()** function is used to store user data. If the user is playing for the first time, a new JSON file is created with user information in *player_info* folder, including *username, matches, losses, wins, loss percentage, win percentage, current streak, max streak, and the results of the first six tries.*

- The **display_player_data()** function is responsible for displaying all user statistics, such as *username, matches, losses, wins, loss percentage, win percentage, current streak, max streak, and the results of the first six tries,* in a table format using tabulate module.

- The **tutorial()** function provides instructions for playing the wordle game.

### test_wordle.py

This file contains all the methods for checking **wordle.py** using the pytest module.