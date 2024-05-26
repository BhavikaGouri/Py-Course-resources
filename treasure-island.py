print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are at crossroads. where do you want to go?")
direction = input("type 'right' or 'left'").lower()
if direction == 'right':
          print("You fell from the hill.Game over")
elif direction == 'left':
          print("You are at the lake. There is an island in the middle of the lake.")
          print("Type 'wait' to wait for the boat. Type 'swim' to swim across")
          choice = input('What do you choose? ').lower()
          if choice == 'wait':
            print("Days passed, you got no boat. Game over")
          elif choice == 'swim':
                    print("You are brave which made you reach the island unharmed. There is a house with 3 doors. One red, one yellow and one blue, choose one.")
                    colour = input("Enter colour 'red', 'yellow' or 'blue'").lower()
                    if colour == 'red':
                              print("You entered a room of fire. Game Over!")
                    elif colour == 'yellow':
                              print("You found the treasure. You win!")
                    elif colour == 'blue':
                              print("You entered a room of beats, Game Over!")
                    else:
                              print("GAME OVER")
          else:
                    print("GAME OVER")
else:
          print("GAME OVER")
          