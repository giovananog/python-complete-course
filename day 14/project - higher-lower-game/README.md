# Higher Lower Game Project

## Overview

The Higher Lower Game project is a simple Python game that allows you to compare the number of followers on Instagram of two randomly selected entities. Your goal is to guess which of the two entities has a higher number of followers. Here's how you can create and enjoy this game:

## Step 1: Project Setup

1. Create a new Python script (e.g., `higher_lower_game.py`) in your code editor.

2. Import the required libraries and data:

```python
import art
from replit import clear
from game_data import data
import random
```

3. Initialize variables and set the initial score:

```python
continue_loop = True
actual_itemA = data[random.randint(0, len(data) - 1)]
score = 0
```

## Step 2: Implement the Game Logic

1. Create a loop to handle the game logic. The player should compare two entities' followers and guess which one has more followers:

```python
while continue_loop:
  print(art.logo)
  print(f"You current score in this game is: {score}\n")
  print(f'Compare A: {actual_itemA["name"]}, a {actual_itemA["description"]}, from {actual_itemA["country"]}')
  print(art.vs)
  actual_itemB = data[random.randint(0, len(data) - 1)]
  print(f'Against B: {actual_itemB["name"]}, a {actual_itemB["description"]}, from {actual_itemB["country"]}')
  answer = input("\n\nWho has more followers? Type 'A' or 'B': ")
```

2. Check if the player's guess is correct, and update the score accordingly:

```python
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
```

3. If the player's guess is incorrect or if they input an invalid option, the game ends:

```python
print(f"You lost the game! Final score: {score}")
```

## Step 3: Wrapping Up

1. After the game ends, ask the player if they want to play again or exit the program.

2. Customize and add more features to enhance the game's enjoyment.

## Step 4: Testing and Enjoyment

1. Run the script and play the game to ensure it works as expected.

2. Challenge your friends and see who can achieve the highest score in the Higher Lower Game you've created!

This project offers a fun way to compare your knowledge about the popularity of various entities on Instagram. Have fun coding and playing the game!
