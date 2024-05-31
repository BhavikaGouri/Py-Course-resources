#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
logo = """
  ______ _     _ _______ _______ _______      _______ _     _ _______      __   _ _     _ _______ ______  _______  ______
 |  ____ |     | |______ |______ |______         |    |_____| |______      | \  | |     | |  |  | |_____] |______ |_____/
 |_____| |_____| |______ ______| ______|         |    |     | |______      |  \_| |_____| |  |  | |_____] |______ |    \_


"""

print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
end_of_game = "false"
num = random.randint(1,100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100. ")
type = input("Select level 'easy' or 'hard' :").lower()

if type == "easy":
  num_of_turns = 10
else:
  num_of_turns = 5

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def compare():
  guess = int(input("\nGuess the number: "))
  global num_of_turns,end_of_game
  num_of_turns -= 1
  if num > guess:
    print("Too Low")
  elif num < guess:
    print("Too High")
  else:
    end_of_game = "true"
    print(f"You guessed it right!,The answer was {num}")
    return
  print(f"\nYou have {num_of_turns} turns left")
    
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
while(end_of_game == 'false'):
  if num_of_turns == 0:
    print("You ran out of turns")
    end_of_game = "true"
    break
  compare()
  
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

