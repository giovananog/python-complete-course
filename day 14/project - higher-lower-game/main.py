import art 
from replit import clear
from game_data import data
import random

continue_loop = True
actual_itemA = data[random.randint(0,len(data)-1)]
score = 0 

while continue_loop:
  print(art.logo)
  print(f"You actual score in this game is: {score}\n")
  print(f'Compare A: {actual_itemA["name"]}, a {actual_itemA["description"]}, from {actual_itemA["country"]}')
  print(art.vs)
  actual_itemB = data[random.randint(0,len(data)-1)]
  print(f'Against B: {actual_itemB["name"]}, a {actual_itemB["description"]}, from {actual_itemB["country"]}')
  answer = input("\n\nWho has more followers? Type 'A' or 'B': ")
  if answer == "A":
    if actual_itemA["follower_count"] >= actual_itemB["follower_count"]:
      clear()
      score += 1
    else:
      continue_loop = False
  elif answer == "B":
    if actual_itemA["follower_count"] <= actual_itemB["follower_count"]:
      actual_itemA = actual_itemB
      clear()
      score += 1
    else:
      continue_loop = False
  else: 
    continue_loop = False 

print(f"You lost the game! Final score was: {score}")
