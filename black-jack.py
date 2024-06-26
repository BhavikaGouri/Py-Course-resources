############### Blackjack Project #####################
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/

import random
play = "true"
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
  
while play == "true":
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  print("Your Cards : ",user_cards,"The sum is : ",sum(user_cards))
  print("Computer's Cards : -- ", computer_cards[0])
  
  choice = input("Want to hit or stand? ").lower()
  
  while(choice == 'hit'):
    if sum(user_cards) > 21:
      break
    user_cards.append(deal_card())
    print(user_cards," The sum is : ",sum(user_cards))
    choice = input("Want to hit or stand? ").lower()
    if choice == 'stand':
      break
  print("Your Cards : ",user_cards)
  
  while(sum(computer_cards) < 17):
    if sum(computer_cards) > 21:
      break
    computer_cards.append(deal_card())
    
  #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
  #and returns the score. 
  #Look up the sum() function to help you do this.
  
  
  def calculate_score(cards):
    sum = 0
    for i in cards:
      sum += i
    if sum == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum > 21:
      sum = sum - 10
      return sum
    return sum
    
    
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  #function to check who is the winner
  
  def Winner(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
      return "Draw"
    elif user_score > computer_score and user_score <= 21:
      return "You Win"
    elif user_score < computer_score and computer_score <= 21:
      return "Dealer Wins"
    elif computer_score > 21:
      return "You Win"
    elif user_score > 21:
      return "Dealer Wins"
    elif user_score == 0:
      return "You Win, BLACKJACK"
    elif computer_score == 0:
      return "Dealer Wins, BLACKJACK"
    else:
      return "Draw"
      
  print("The Result is : ", Winner(user_score, computer_score)) 
  print("\n",user_score," = ", user_cards,"\n")
  print(computer_score, " = ", computer_cards)

  #if user wants to continue playing
  
  play = input("Want to play again? 'true' or 'false' ").lower()
  if play == 'true':
    continue
  else:
    break