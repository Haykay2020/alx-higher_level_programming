#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
             'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    length = len(roman_string)
    num = roman[roman_string[length - 1]]

    for i in range(length - 2, -1, -1):
        if roman[roman_string[i]] >= roman[roman_string[i + 1]]:
            num += roman[roman_string[i]]
        else:
            num -= roman[roman_string[i]]
    return num
