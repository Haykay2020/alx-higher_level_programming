#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [5, 6, 7, 8, 9, 10]
idx = 5
print("value at index {:d} is {}".format(idx, element_at(my_list, idx)))
