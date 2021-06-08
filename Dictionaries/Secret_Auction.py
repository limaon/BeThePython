import os
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bindding_record):
    highest_bid = 0
    winner = ""
    for bidder in bindding_record:
        bid_amount = bindding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
