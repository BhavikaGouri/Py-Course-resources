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
import random
list = ['rock','paper','scissors']
index = random.randint(0,2)
computer = list[index]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user == 0:
    print("Rock")
    print(rock)
    print("\nComputer chose:\n")
    if computer == 'rock':
        print(rock)
        print("It's a draw")
    elif computer == 'paper':
        print(paper)
        print("You lose")
    else:
        print(scissors)
        print("You Win")
elif user == 1:
    print("Paper")
    print(paper)
    print("\nComputer chose:\n")
    if computer == 'rock':
        print(rock)
        print("You Win")
    elif computer == 'paper':
        print(paper)
        print("It's a draw")
    else:
        print(scissors)
        print("You lose")
elif user == 2:
    print("Scissors")
    print(scissors)
    print("\nComputer chose:\n")
    if computer == 'rock':
        print(rock)
        print("You lose")
    elif computer == 'paper':
        print(paper)
        print("You Win")
    else:
        print(scissors)
        print("It's a draw")
else:
    print("Invalid Prompt")