#!/usr/bin/python3
# LAGRE GABBA BERTRAND
# https://github.com/FoubaDev

if __name__ == "__main__":
    import sys

    length = len(sys.argv)-1
    if length == 0:
        print("0 arguments.")
    else:
        print(f"{length} argument{'s' if length != 1 else ''}:")
        i = 1
        for arg in sys.argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1
