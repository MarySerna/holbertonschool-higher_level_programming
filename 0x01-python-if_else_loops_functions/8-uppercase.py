#!/usr/bin/python3
def uppercase(str):
    for j in str:
        if ord(j) >= 97 and ord(j) <= 123:
            j = (ord(j) - 32)
        else:
            j = ord(j)
        print("{:c}".format(j), end="")
    print("")
