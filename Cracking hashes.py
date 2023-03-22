"""
Name: Cracking Hashes
Arthur: Nils Arne Topland
Date created: 22.03.2023
"""
import hashlib

Hash_given = "INSERT HASH CODE HERE"

with open("pass.txt") as my_text:
    """ Add passwords to pass.txt or use rockyou.txt as password file"""
    List = my_text.readline()

    for i in List:
        hashes = hashlib.sha3_512(i.strip().encode()).hexdigest()
        if hashes == Hash_given:
            print(i)

"""
Note hashes = hashlib.HASH_xyz must be changed to match hash type
"""
