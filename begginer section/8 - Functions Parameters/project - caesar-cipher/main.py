from replit import clear
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caeser(text, shift, dir):
  text = list(text)
  for i in text:
    index = alphabet.index(i)
    if dir == "encode":
      shift_change = index + shift
      if shift_change >= 26:
         shift_change -= 26
    elif dir == "decode":
      shift_change = index - shift
      if shift_change < 0:
         shift_change += 26
    text[text.index(i)] = alphabet[shift_change]
  print(''.join(text))

continue_program = True
print(logo)

while continue_program:
  continue_program = input("\n\nDo you want to encode/decode a new word? (y/n):  ")
  if continue_program == "y":
    clear()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
  elif continue_program == "n":
    continue_program = False
  else:
    print("invalid input, try again!")

