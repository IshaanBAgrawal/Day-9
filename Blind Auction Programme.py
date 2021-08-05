from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
bid_of_everyone = {}
def auctioneer(name_of_bidder, bidding):
  global bid_of_everyone
  bid_of_everyone[name_of_bidder] = bidding

print(logo)
print("Welcome to the secret auction program.")

more_bidders = "yes"
while more_bidders == "yes":
  name = input("What is your name?: ")
  bid = int(input("What's your bid? $"))
  auctioneer(name, bid)
  more_bidders = input("Are there more bidders? Type 'yes'or 'no'. ").lower()
  clear()

highest_bid = 0
highest_bidder = ""
if more_bidders == 'no':
  for key in bid_of_everyone:
    if highest_bid < bid_of_everyone[key]:
      highest_bid = bid_of_everyone[key]
      highest_bidder = key
print(f"The winner is {highest_bidder}, with a bid of ${highest_bid}.")
