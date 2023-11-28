#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) - 32) in range(ord('A'), ord('Z')+1):
            str = str.replace(c, chr(ord(c)-32))
    print("{}".format(str))
