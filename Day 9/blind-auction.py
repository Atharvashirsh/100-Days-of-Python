# Print the logo
from art import logo

print(logo)

blind_auction = {}

ifNewPerson = True


def highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""

    for person in bidding_records:
        if bidding_records[person] > highest_bid:
            highest_bid = bidding_records[person]
            winner = person

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while ifNewPerson:
    print("Welcome to the secret auction program.")
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    blind_auction[name] = bid

    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "no":
        ifNewPerson = False

highest_bidder(blind_auction)
