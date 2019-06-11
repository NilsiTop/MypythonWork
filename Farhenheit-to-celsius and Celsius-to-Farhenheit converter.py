"""
** Name: ** Fahrenheit-to-celsius and Celsius-to-fahrenheit converter.py*
** Created on ** 11 June 2019*
** Author: ** Nils Arne Topland*
"""


def fahrenheit_to_celsius(user):
    return (user - 32)*5/9


def celsius_to_fahrenheit(user2):
    return (user2 * 9/5) + 32


def menu():
    print("1 to Convert Fahrenheit to Celsius")
    print("2 to Convert Celsius to Fahrenheit")
    print("3 to exit program")
    while True:
        try:

            selection = float(input("Please select a option from menu :"))
            if selection == 1:
                user = float(input("Enter Fahrenheit(F):"))
                fahrenheit_to_celsius(user)
                print(float(fahrenheit_to_celsius(user)), "Celsius, C")
                menu()
            elif selection == 2:
                user2 = float(input("Enter a temperature in Celsius:"))
                celsius_to_fahrenheit(user2)
                print(float(celsius_to_fahrenheit(user2)), "Fahrenheit, F")
                menu()
            if selection == 3:
                break
        except ValueError:
            print("Use number 1 - 3")


if __name__ == '__main__':
    menu()



