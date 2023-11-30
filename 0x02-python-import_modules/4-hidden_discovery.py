#!/usr/bin/python3
# LAGRE GABBA BERTRAND
# https://github.com/FoubaDev

import hidden_4
import dis

if __name__ == "__main__":

    content = dir(hidden_4)
    for i in content:
        if i[:2] != "__":
            print(i)
