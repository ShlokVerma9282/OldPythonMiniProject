import os

bids = {}
bidding_finished = False

def clear(): os.system('cls')

def find_highest_bidder(bidding_record):
  max_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > max_bid: 
      max_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${max_bid}")

while not bidding_finished:
  name = input("What is your name?:\n")
  price = int(input("What is your bid?:\n$"))
  bids[name] = price
  loop =True
  while loop:
   ask = input("Are there any other bidders? Type 'Yes or 'No'.\n")
   ask.lower()
   if ask == "no":
     bidding_finished = True
     find_highest_bidder(bids)
     loop= False
   elif ask == "yes":
     clear()
     loop=False
   elif ask!="yes"or"no":
     print("Invalid Input")
     print("Try Again\n\n")
      
  
