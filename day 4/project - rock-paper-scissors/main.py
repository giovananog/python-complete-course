import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]
option = int(input("Choose rock (0), paper (1), scissors (2): "))

print("\nYou chose:")
print(options[option])

print("\nComputer chose: \n")
computer_choice = random.randint(0,2)
print(options[computer_choice])

if (option == computer_choice):
  print("The game tied")
elif ((option == 0 and computer_choice == 1)or(option == 1 and computer_choice == 2)or(option == 2 and computer_choice == 0)):
  print("You lose")
else:
  print("You won!")
