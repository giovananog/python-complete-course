from replit import clear
from art import logo

persons_and_bids = {}
print(f"{logo}\nWelcome to the auction program! \n")

other = True 

while other:
  name = input("What is your name? \n")
  bid = int(input("What is your bid? \n"))
  other = input("Are there any other bidders? Type 'yes' or 'no' \n")
  
  if other == "yes":
    clear()
  elif other == "no":
    other = False
  else:
    print("Invalid input, try again... \n")
    
  persons_and_bids[name] = bid

higher = 0
person = ""
for i in persons_and_bids:
  if persons_and_bids[i] > higher:
    higher = persons_and_bids[i]
    person = i


clear()
print(f"The winner is {person} with a bid of {higher}")
