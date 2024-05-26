#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
type = input("Enter level 'easy' or 'hard'").lower()

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ''
list = []
if type == 'hard':
  for i in range(nr_letters):
    index1 = random.randint(0,len(letters)-1)
    list.append(letters[index1])
  for i in range(nr_numbers):
    index2 = random.randint(0,len(numbers)-1)
    list.append(numbers[index2])
  for i in range(nr_symbols):
    index3 = random.randint(0,len(symbols)-1)
    list.append(symbols[index3])
  random.shuffle(list)
  for i in list:
    password += i

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
elif type == 'easy':
  for i in range(nr_letters):
    index1 = random.randint(0,len(letters)-1)
    password += letters[index1]
  for i in range(nr_numbers):
    index2 = random.randint(0,len(numbers)-1)
    password += numbers[index2]
  for i in range(nr_symbols):
    index3 = random.randint(0,len(symbols)-1)
    password += symbols[index3]
else:
  print("Invalid Type")
print(password)
