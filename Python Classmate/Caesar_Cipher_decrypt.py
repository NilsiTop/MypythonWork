"Date writen: 09.11.2019"
"File Name: Caesar Cipher_UserInput.py"
"Artur: Nils Arne Topland"

# Reference WebCraftie

message = input("Enter encrypted text :")
message = message.lower()
shiftValue = int(input("\nEnter a Shift Value : "))
encryptionMsg = ""

for character in message:
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
