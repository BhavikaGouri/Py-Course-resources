#Write your code below this line 👇
print("Welcome to bill calculator! ")
bill = float(input("Enter your total bill: $"))
tip = int(input("Enter the percentage of tip you want to give[10,12 or 20]: "))
people = int(input("Enter the number of people to split the bill: "))
tip_percentage = tip/100
total_tip = bill * tip_percentage
split = round((bill + total_tip)/people,3)
print(f"Each person should pay: ${split}")