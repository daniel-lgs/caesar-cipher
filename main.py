from art import logo
from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(message, shift_number, direction_option):
    new_message = ""
    for letter in message:
        if letter in alphabet:
            index_of_letter = alphabet.index(letter)
            for i in range(shift_number):
                if direction_option == "encode":
                    if index_of_letter+1 >= len(alphabet):
                        index_of_letter = 0
                    else:
                        index_of_letter += 1
                else:
                    if index_of_letter-1 < 0:
                        index_of_letter = len(alphabet)-1
                    else:
                        index_of_letter -= 1
            new_message += alphabet[index_of_letter]
        else:
            new_message += letter
    message = new_message
    if direction_option == "encode":
        print(f"The encoded text is {message}")
    else:
        print(f"The decoded text is {message}")

run = True

while run == True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    if input("Run again? Type 'yes' or any key to close :\n") != 'yes':
        run = False
    clear()
   
