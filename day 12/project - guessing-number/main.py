from art import logo
import random

print(logo)

game_over = False
difficulty = False
number = random.randint(0,101)
print(number)
print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.\n\n")


while(difficulty != "easy" and difficulty != "hard"):
   difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
   if difficulty == "easy":
     chances = 10
   else:
     chances = 5
   

while chances > 0:
   guess = int(input(f"\nYou have {chances} remaining to guess the number\nMake a guess: "))
   chances -= 1
   if guess < number:
     print("Too low")
   elif guess > number: 
     print("Too high")
   else:
     print(f"You won! The number was {number}")
     chances = -2

if chances == 0: 
  print(f"\nYou lost! The number was {number}")
