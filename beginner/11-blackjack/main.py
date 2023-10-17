############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
from random import choice
# from replit import clear
from art import logo


def deal_card():
    """returns a card from cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def find_ace(cards):
    """removes 11 form cards and adds 1 to it if the total of cards is greater than 21"""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)


def game_result(player_cards, computer_cards):
    print(f"Your final hand: {player_cards}, Final Score: {sum(player_cards)}")
    print(
        f"Computer's final hand: {computer_cards}, Final Score: {sum(computer_cards)}"
    )
    if sum(player_cards) == sum(computer_cards):
        return "Draw"
    elif sum(computer_cards) == 21:
        return "You lose"
    elif sum(player_cards) == 21:
        return "You Win"
    elif sum(player_cards) > sum(computer_cards) and sum(player_cards) > 21:
        return "You went over. You lose."
    elif sum(player_cards) < sum(computer_cards) and sum(player_cards) < 21:
        return "You Win."
    else:
        return "Opponent went over. You win."


while True:
    play = input(
        "Do you want to play the game of BLACKJACK 'y' or 'n': ").lower()
    if play == "y":
        # clear()
        print(logo)
        player_cards = []
        computer_cards = []

        for i in range(2):
            player_cards.append(deal_card())
            computer_cards.append(deal_card())

        while True:
            find_ace(player_cards)
            find_ace(computer_cards)

            print(
                f"Your Cards: {player_cards}, Current Score: {sum(player_cards)}"
            )
            print(f"Computer's first card: {computer_cards[0]}")

            if sum(player_cards) >= 21:
                print(game_result(player_cards, computer_cards))
                break
            elif sum(player_cards) < 21:
                should_continue = input(
                    "Type 'y' to get another card, type 'n' to pass: ").lower(
                    )
                if should_continue == "y":
                    player_cards.append(deal_card())
                    computer_cards.append(deal_card())
                    continue
                elif should_continue == 'n':
                    print(game_result(player_cards, computer_cards))
                    break
                else:
                    break
            else:
                break
    elif play == 'n':
        break
    else:
        exit()
