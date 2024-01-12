import random
import hangman_words
import hangman_art
from replit import clear

hangman_art.stages.reverse()
actual_stage = 0
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(hangman_art.logo)
display = []

for _ in range(0, len(chosen_word)):
  display.append("_")

won = False

while display.count("_") > 0 and not won:  
  print(hangman_art.stages[actual_stage])
  print(f"\n{' '.join(display)}\n")
  guess = input("\nGuess a letter: ").lower()
  if guess not in chosen_word:
    if actual_stage == len(hangman_art.stages)-1:
       won = True
    actual_stage += 1
  else: 
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
  clear()
  

if not won:
  print("\n\nYou won the game!!!")
else:
  print(f"\n\nYou lose the game!!! The word was {chosen_word}")
  