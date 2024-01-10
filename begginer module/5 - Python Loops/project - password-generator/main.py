#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
psw = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(0, nr_letters):
  psw += letters[random.randint(0,len(letters)-1)]
for i in range(0, nr_symbols):
  psw += symbols[random.randint(0,len(symbols)-1)]
for i in range(0, nr_numbers):
  psw += numbers[random.randint(0,len(numbers)-1)]

# aq dava pra usar random.choice(lista) q escolhe um elemento aleatorio da lista


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_psw = ""

# for i in range(0,len(psw)):
#   hard_psw[i] = ""

j = 0
while j != len(psw):
  random1 = random.randint(0,len(psw)-1)
  if (hard_psw.count(psw[random1]) == 0):
    hard_psw += psw[random1]
    j+=1


easy_or_hard = int(input("\n\nEasy(0) or Hard(1) password? "))
if easy_or_hard == 0:
  print(psw)
else:
  print(hard_psw)
  # dava pra fazer simplesmente um random.shuffle(psw)
