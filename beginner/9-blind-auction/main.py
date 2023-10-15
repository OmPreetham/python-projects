from replit import clear
from art import logo

#HINT: You can call clear() to clear the output in the console.

print(logo)


def find_highest_bidder(bids):
    winning_bid = 0
    for bid in bids:
        current_bid = bids[bid]
        if current_bid > winning_bid:
            winning_bid = current_bid
            winner = bid
    print(f"And the WINNER is {winner} with bid of ${winning_bid}")


auction_status = True
bids = {}

while auction_status:
    bidder_name = input("Enter your name: ")
    bidder_amount = float(input("Enter bidding amount in american $: "))
    bids[bidder_name] = bidder_amount
    yn = input("Are there any other bidders? (y/n): ").lower()
    clear()
    if yn == 'y':
        continue
    else:
        find_highest_bidder(bids)
        auction_status = False
