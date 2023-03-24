"""
** Name: ** fibonacci.py*
** Created on ** 09 June 2019*
** Author: ** Nils Arne Topland*
"""


def fibonacci(n):
    a, b, counter = 0, 1, 0

    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


for x in fibonacci(300):
    print("Generated:", x)
