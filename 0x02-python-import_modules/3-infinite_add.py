#!/usr/bin/python3
# LAGRE GABBA BERTRAND
# https://github.com/FoubaDev

if __name__ == "__main__":

    import sys
    length = len(sys.argv)-1
    if length == 0:
        print(0)
    else:
        summ = 0
        for arg in sys.argv[1:]:
            summ += int(arg)
        print(summ)
