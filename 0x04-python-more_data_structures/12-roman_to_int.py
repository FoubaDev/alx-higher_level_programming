#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = 0
        for i in roman_string:
            if i in dic:
                int_value += dic[i]
            else:
                return 0
        return int_value
    else:
        return 0
