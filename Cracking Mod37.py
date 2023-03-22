"""
Name: Cracking Mod37 Hash
Arthur: Nils Arne Topland
Date created: 22.03.2023
"""

Library = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
List = []
"""
Add any hexvalues such as 206, 293, 389, 325, etc in list
"""
for i in List:
    print(Library[i % 37], end="")

