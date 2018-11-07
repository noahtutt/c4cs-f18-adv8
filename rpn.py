#!/usr/bin/env python3
# this is a test comment
import operator
from colorama import Fore, Style, Back
from sys import argv
import readline

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def color_print(token):
    try:
         token = int(token)
         if token < 0:
             print(Fore.RED + str(token), end=" ")
         else:
             print(Fore.BLUE + str(token), end=" ")
    except ValueError:
         print(Fore.MAGENTA + token, end=" ")


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
        if len(argv) != 1:
            print(stack)    
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        usr_in = input("rpn calc> ")
        print("Evaluating the expression:", end=" ")
        print(Back.WHITE + Style.BRIGHT, end="")
        for token in usr_in.split():
            color_print(token)
        print(Style.RESET_ALL)
        result = calculate(usr_in)
        print("Result:", end=" ")
        color_print(result)
        print(Style.RESET_ALL)
        print("")

if __name__ == '__main__':
    main()
