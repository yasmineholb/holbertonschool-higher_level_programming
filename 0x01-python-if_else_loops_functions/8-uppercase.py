#!/usr/bin/python3
def uppercase(str):
    z = ""
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            x = ord(i) - 32
            y = chr(x)
            z = z + y
        else:
            z = z + i
    print("{}".format(z))
