"Date 15.11.2019"
"File Name: Convert hex_string_to_binary.py"
"Artur: Nils Arne"

# User Input
string = input("Enter string or a letter :")

print("The string Is =", string)

# Remove 008b from string
Convert = "{0:08b}".format(int(string, 16))

print("Result Is", str(Convert))
