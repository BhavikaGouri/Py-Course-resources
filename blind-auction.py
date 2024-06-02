import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


bid_dict = {}
init_choice = input("Type 'yes' if you want to bid, otherwise type 'no'.\n'").lower()
choice = init_choice
while(choice == 'yes'):
  name = input("What is your name? :")
  bid = input("What is your bid? $")
  choice = input("Want to bid more? Type 'yes' or 'no'").lower()
  def add_bid(name, bid):
    bid_dict[name] = bid
  add_bid(name,bid)
  os.system('clear')
  if choice == 'no':
    break

def winner_bid():
  max_bid = 0
  max_bidder = ""
  
  if bid_dict == {}:
    print("Atleast one bid is required")
  else:
    for bidder in bid_dict:
      if max_bid < int(bid_dict[bidder]):
        max_bid = int(bid_dict[bidder])
        max_bidder = bidder
  
    print(f"The winner is {max_bidder} with a bid of ${max_bid}")
winner_bid()
