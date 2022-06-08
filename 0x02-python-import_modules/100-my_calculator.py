#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # check usage
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, op, b = sys.argv[1:]

    # choose operation
    if op == '+':
        func = add
    elif op == '-':
        func = sub
    elif op == '*':
        func = mul
    else:
        func = div

    # perfom calculation and print result
    print("{} {} {} = {:d}".format(a, op, b, func(int(a), int(b))))
