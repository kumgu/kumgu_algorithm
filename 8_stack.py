'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is Empty...1")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty...2")

    def __len__(self):
        return len(self.items)

    def isBalanced(self, expr):
        for p in expr:
            if p in [ '(', '{', '[' ]:
                S.push(p)
            elif p == ')':
                if S.top() == '(':
                    S.pop()
                else:
                    return False
            elif p == '}':
                if S.top() == '{':
                    S.pop()
                else:
                    return False
            elif p == ']':
                if S.top() == '[':
                    S.pop()
                else:
                    return False
        return True

S = Stack()
expr = input()

if S.isBalanced(expr):
    print("Balanced")
else:
    print("Not Balanced")
            
'''

# GeeksforGeeks

def areBracketBalanced(expr):
    stack = []

    for char in expr:
        if not stack:
            return False
        if char in [ '(', '{', '[' ]:
            stack.append(char)
        else:
            current_char = stack.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '{':
                if char != '}':
                    return False
            if current_char == '[':
                if char != ']':
                    return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = input()

    if areBracketBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")