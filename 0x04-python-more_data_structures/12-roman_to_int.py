#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    
    roman_nums = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}
    last_value = 0
    s = 0

    for x in reversed(roman_string):
        n = roman_nums.get(x, 0)
        if n < last_value:
            s -= n
        else:
            s += n
        last_value = n

    return s
