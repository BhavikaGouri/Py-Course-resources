logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' and 'decrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(t, s):
    cipher_text = ""
    for i in t:
        if i == ' ':
            cipher_text += i
        if i in alphabet:
            index = alphabet.index(i)
            if index + s > 25:
                index = index - 26
            cipher_text += alphabet[index + s]
        else:
            cipher_text += i
    print("Here's your code : ", cipher_text)


def decrypt(t, s):
    original = ""
    for i in t:
        if i == ' ':
            original += i
        if i in alphabet:
            index = alphabet.index(i)
            if index - s < 0:
                index = index + 26
            original += alphabet[index - s]
        else:
            original += i
    print("Here's your decoded code : ", original)


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

while (1):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Invalid prompt")

    continuation = input("Want to continue further type 'yes' or 'no' : ")
    if continuation == 'yes':
        continue
    else:
        break
