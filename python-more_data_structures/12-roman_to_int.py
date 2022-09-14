#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or :
        return 0
    rvalue = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    for i in range(len(roman_string)):
        if i > 0 and rvalue[roman_string[i]] > rvalue[roman_string[i - 1]]:
            int_value += rvalue[roman_string[i]] - 2 * rvalue[roman_string[i - 1]]
        else:
            int_value += rvalue[roman_string[i]]
    return int_value
