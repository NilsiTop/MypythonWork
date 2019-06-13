"""
** Name: ** Portscanner.py*
** Author: ** Nils Arne Topland*
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("Enter Target IP: ")
print("\n -----Please wait. Scan presses is a about  to start ---------------")


def pcscan(port):

    try:
        sock.connect((target, port))
        return True
    except:
        return False


for x in range(1, 1025):
    if pcscan(x):
        print('*' 'Port', x, 'is open')

    else:
        print('*' "port", x, "is open")



