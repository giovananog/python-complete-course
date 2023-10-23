from art import logo
from replit import clear

print(logo)

def calculator(operation, number1, number2):
  actual_number = 0
  if operation == "+":
    actual_number = number1 + number2
  elif operation == "-":
    actual_number = number1 - number2
  elif operation == "*":
    actual_number = number1 * number2
  elif operation == "/":
    actual_number = number1 / number2
  else:
    return "invalid input of operator."
    
  print(f"\n{number1} {operation} {number2} = {actual_number}\n\n")
  return actual_number


continue_loop = True
break_coninue_loop = True

while continue_loop:
  if break_coninue_loop:
    number1 = float(input("\nWhat is the first number?: ")) 
    print("\n+\n-\n*\n/")
  operation = input("\nPick an operation: ")
  number2 = float(input("\nWhat is the next number?: "))
  actual_number = calculator(operation, number1, number2)
  continue_loop = input(f"Do you want to continue calculating with {actual_number} ('y') or start a new calculation ('n')? (press any other key to leave the program): ")
  if continue_loop == "y":
    number1 = actual_number
    break_coninue_loop = False
  elif continue_loop == "n":
    break_coninue_loop = True
    clear()
  else:
    continue_loop = False
  
