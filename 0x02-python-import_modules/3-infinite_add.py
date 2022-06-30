#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add_arg = 0
    for i in argv[1:]:
        add_arg += int(i)
    print("{:d}".format(add_arg))
