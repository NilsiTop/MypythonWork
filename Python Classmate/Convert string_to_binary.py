"Date 15.11.2019"
"File Name: Convert string_to_binary.py"
"Artur: Nils Arne"

string = input("Enter text: ")
print("The String is As follows : ", str(string))

# Conversion is done with bytearry function

res = ''.join(format(i, 'b') for i in bytearray(string, encoding ='utf-8'))

print("The String is converted to binary :" + str(res))

