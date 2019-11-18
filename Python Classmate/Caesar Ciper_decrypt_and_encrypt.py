"Date writen: 17.11.2019"
"File Name: Caesar Cipher_encypt and decrypt.py"
"Artur: Nils Arne Topland"


def mainMeny():
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Quit")
    while True:
        try:
            selection = int(input("Enter choice:"))
            if selection == 1:
                 encryption()
                 break
            elif selection == 2:
                 Decrypt()
                 break
            elif selection == 3:
                break
            else:
                print("invalid choice. Enter 1 - 3")
                mainMeny()
        except ValueError:
            print("Invalid choice, Enter number 1 - 3")
#    exit


def encryption():
    message = input("Enter text to encrypt :")
    message = message.lower()
    shiftvalue = int(input("\nEnter a Shift Value : "))
    encryptionmsg = ""

    for character in message:
        if character.isalpha() == True:
            if character == character.lower():
                x = ord(character) - 97
                x += shiftvalue
                x = x % 26
                encryptionmsg += chr(x + 97)
            else:
                x = ord(character) - 65
                x += shiftvalue
                x = x % 26
                encryptionmsg += chr(x + 65)
        else:
            encryptionmsg += character
            print("The result is =", encryptionmsg)
 #       anykey = input("Enter any character to return to main menu:")
    mainMeny()


def Decrypt():
    Decrypt_message = input("Enter encrypted text :")
    Decrypt_message = Decrypt_message.lower()
    shiftValue = int(input("\nEnter a Shift Value : "))
    encryptionMsg = ""

    for character in Decrypt_message:
        if character.isalpha() == True:
            if character == character.lower():
                x = ord(character) - 97
                x -= shiftValue
                x = x % 26
                encryptionMsg += chr(x + 97)
            else:
                x = ord(character) - 65
                x -= shiftValue
                x = x % 26
                encryptionMsg += chr(x + 65)
        else:
            encryptionMsg += character
            print("The result is = ", encryptionMsg)

#        anykey = input("Enter any character to return to main menu:")
    mainMeny()


mainMeny()

