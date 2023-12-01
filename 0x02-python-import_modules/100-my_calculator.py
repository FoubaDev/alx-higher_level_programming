#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    # declare a dictionary for functions
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    # check if the 2nd argument is an operator
    op_list = ['+', '-', '*', '/']
    if sys.argv[2] not in op_list:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a, b = int(sys.argv[1]), int(sys.argv[3])
    func_dict = {'+': add, '-': sub, '*': mul, '/': div}
    get_key = func_dict[sys.argv[2]]
    print("{} {} {} = {}".format(a, sys.argv[2], b, get_key(a, b)))
