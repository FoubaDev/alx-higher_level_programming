#!/usr/bin/python3
# Find the position of a and z
for ch in range(ord('a'), ord('z')+1):
    if chr(ch) in ['q', 'e']:
        pass
    else:
        print("{}".format(chr(ch)), end="")
