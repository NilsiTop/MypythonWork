"""
** Name: ** Calculator.py**
** Created on ** 09 June 2019**
** Author: ** Nils Arne Topland**
"""


def mainMeny():
    print("1. Subtract")
    print("2. Multiplication")
    print("3. Addition")
    print("4. Divide")
    print("5. Quit")
    while True:
        try:
            selection = int(input("Enter choice:"))
            if selection == 1:
                num1 = float(input("Enter 1st number:"))
                num2 = float(input("Enter 2nd Number:"))
                subtract(num1, num2)
                print('Sum =', subtract(num1, num2))
                mainMeny()

            elif selection == 2:
                num1 = float(input("Enter 1st number:"))
                num2 = float(input("Enter 2nd Number:"))
                multiplication(num1, num2)
                print("Sum =", multiplication(num1, num2))
                mainMeny()

            elif selection == 3:
                num1 = float(input("Enter 1st number:"))
                num2 = float(input("Enter 2nd Number:"))
                addition(num1, num2)
                print("Sum =", addition(num1, num2))
                mainMeny()

            elif selection == 4:
                num1 = float(input("Enter 1st number:"))
                num2 = float(input("Enter 2nd Number:"))
                divide(num1, num2)
                print("Sum =", divide(num1, num2))
                mainMeny()

            elif selection == 5:
                print("Goodbye")
                break
            else:
                print("invalid choice. Enter 1 - 5")
                mainMeny()
        except ValueError:
            print("Invalid choice, Enter number 1 - 5")


def subtract(num1, num2):
    return float(num1) - float(num2)


def multiplication(num1,num2):
    return float(num1) * float(num2)


def addition(num1, num2):
    return float(num1) + float(num2)


def divide(num1, num2):
    return float(num1)/float(num2)


if __name__ == '__main__':
    mainMeny()
