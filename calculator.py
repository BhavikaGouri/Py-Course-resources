logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  
| |_________________| | 
|  ___ ___ ___   ___  | 
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| | 
| | . | 0 | = | | / | |
| |___|___|___| |___| |  
|_____________________|
"""
print(logo)
result = 0

def add(n1,n2):
  return(n1+n2)
def subtract(n1,n2):
  return(n1-n2)
def multiply(n1,n2):
  return(n1*n2)
def divide(n1,n2):
  return(n1/n2)
  
dict = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
  operand1 = float(input("Enter first number :"))
  
  while(True):
    print("+\n-\n*\n/")
    operator = input("Enter operator :")
    operand2 = float(input("Enter second number :"))
    for i in dict:
      if i == operator:
        result = dict[i](operand1,operand2)
    print(f"{operand1} {operator} {operand2} = {result}")
    choice = input("Do you want to continue? type 'y' or 'n' or start 'new' calculation: ").lower()
   
    if choice == 'y':
      operand1 = result
    elif choice == 'new':
      calculator()
    else:

      break

calculator()