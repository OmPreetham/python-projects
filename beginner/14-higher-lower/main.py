from game_data import data
from art import logo, vs
import random


def pick_person():
    person = random.choice(data)
    name = person["name"]
    follower_count = person["follower_count"]
    description = person["description"]
    country = person["country"]
    return name, description, country, follower_count


def compare(follower_count_1, follower_count_2):
    if follower_count_2 > follower_count_1:
        return "h"
    else:
        return "l"


def game():
    print(logo)
    score = 0
    persons = []

    for i in range(2):
        persons.append(pick_person())
    while True:
        if persons[0][0] == persons[1][0]:
            persons.pop(0)
            persons.append(pick_person())

        print(f"\nYou're right!!, Score: {score}")

        print(f"\n{persons[0][0]}, a {persons[0][1]}, from {persons[0][2]}")

        print(vs)

        print(f"\n{persons[1][0]}, a {persons[1][1]}, from {persons[1][2]}")

        follower_count_1 = persons[0][3]
        follower_count_2 = persons[1][3]

        compared = compare(follower_count_1, follower_count_2)
        print(f"\n'{persons[0][0]}' has {follower_count_1}m followers. ")
        user_guess = input(
            f"'{persons[1][0]}' has Higher 'H' or Lower 'L' followers than {persons[0][0]}: "
        ).lower()
        if user_guess == compared:
            score += 1
            persons.pop(0)
            persons.append(pick_person())
        else:
            print(f"Sorry, That's wrong. Your Final Score: {score}")
            return False


game()