# techie delight 
# Convert an infix expression into a postfix expression

import sys
from collections import deque

def prec(c):
    if c == '*' or c == '/':
        return 3
    if c == '+' or c == '-':
        return 4
    # 비트연산자는 나중에 다시
    if c == '&':
        return 8
    if c == '^':
        return 9
    if c == '|':
        return 10
    return sys.maxsize

# Utility function to check if a given token is an operand
def isOperand(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')

def infixToPostfix(infix):
    # base case
    if not infix or not len(infix):
        return True   
    # create an empty stack for storing operators
    s = deque()
    # create a string to store the postfix expression
    postfix = ''
    for c in infix:
        if c == '(':
            s.append(c)
        elif c == ')':
            # pop tokens from the stack until the corresponding 
            # opening bracket '(' is removed.
            #  Append each operator at the end of the postfix expression
            while s[-1] != '(':
                postfix += s.pop()
            s.pop()
        # If the current token is an operand, 
        # append it at the end of the postfix expression
        elif isOperand(c):
            postfix += c
        # If the current token is an operator
        else:
            # remove operators from the stack with higher 
            # or equal precedence and append them
            # at the end of the postfix expression
            while s and prec(c) >= prec(s[-1]):
                postfix += s.pop()
            # finally, push the current operator on top of the stack
            s.append(c)
    # append any remaining operators in the stack 
    # at the end of the postfix expression
    while s:
        postfix += s.pop()
    return postfix

if __name__ == "__main__":
    infix = input()
    postfix = infixToPostfix(infix)
    print(postfix)
   