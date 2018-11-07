#!/usr/bin/env python3
# this is a test comment
import operator
from colorama import Fore, Style


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)    
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        usr_in = input("rpn calc> ")
        print("Evaluating the expression", end=" ")
        for token in usr_in.split():
            try:
                token = int(token)
                if token < 0:
                    print(Fore.RED + str(token) + Style.RESET_ALL, end=" ")
                else:
                    print(Fore.BLUE + str(token) + Style.RESET_ALL, end=" ")
            except ValueError:
                print(Fore.MAGENTA + token + Style.RESET_ALL, end=" ")
        print("")
        result = calculate(usr_in)
        print("Result: ", result)

if __name__ == '__main__':
    main()
