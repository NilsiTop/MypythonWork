"""
** Name: ** mile to km/h, km/h to meter/second converter and visa versa.py*
** Created on ** 11 June 2019*
** Author: ** Nils Arne Topland*
"""


def kmh_to_ms(input1):
    return input1 * 0.277778


def ms_to_kmh(input2):
    return input2 * 3.6


def kmh_to_mph(input3):
    return input3 * 0.6213711922


def mph_to_kmh(input4):
    return input4 * 1.609344


def menu():
    print("1. Convert kilometer pr hour [km/h] to meter/second [m/s]")
    print("2. Convert meter/second [m/s] to kilometer pr hour [km/h]")
    print("3. Convert kilometer/hour [km/h] to Mile/hour [mi/h]")
    print("4. Convert Mile/hour [mi/h] to kilometer/hour [km/h]")
    print("5. Exit program")

    while True:
        try:
            selection = int(input("Enter choice:"))
            if selection == 1:
                input1 = float(input("Type in value to convert kilo meter pr hour to meter pr second: "))
                kmh_to_ms(input1)
                print("\n", input1, "Km/h equal", (kmh_to_ms(input1)), "m/s")
                menu()

            elif selection == 2:
                input2 = float(input("Type in value to convert meter/second [m/s] to kilometer pr hour [km/h] :"))
                ms_to_kmh(input2)
                print("\n", input2, "m/s equal", (ms_to_kmh(input2)), "km/h")
                menu()

            elif selection == 3:
                input3 = float(input("Type in value to convert kilometer pr hour [km/h] to Mile/hour [mi/h]"))
                kmh_to_mph(input3)
                print("\n", input3, " km/h equal", (kmh_to_mph(input3)), "mi/h")
                menu()

            elif selection == 4:
                input4 = float(input("Type in value to convert Mile/hour [mi/h] to kilometer/hour [km/h]"))
                mph_to_kmh(input4)
                print("\n", input4, "mi/h equal", (mph_to_kmh(input4)), "km/h")
                menu()

            if selection == 5:
                print("Goodbye")
                break

        except ValueError:
            print("use number 1 - 5")


if __name__ == '__main__':
    menu()
