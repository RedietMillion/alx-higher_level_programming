#!/usr/bin/python3
j = 122
while j >= 97:
    fl = 0
    if j % 2 != 0:
        j = j - 32
        fl = 1
    print("{:s}".format(chr(j)), end="")
    if fl == 1:
        j = j + 32
    j = j - 1
