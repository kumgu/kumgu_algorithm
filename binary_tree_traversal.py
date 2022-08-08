from collections import deque

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTreeTraversal:
    def inorderIterative(self, root):
        # create an empty stack
        stack = deque()
        # start from the root node(set current node to the root node)
        curr = root
        while stack or curr:
            # if the current node exists, 
            # push it into the stack (defer it)
            # and move to its left child
            if curr:
                stack.append(curr)
                curr = curr.left
            # otherwise, if the current node is None, 
            # pop an element from the stack,
            # print it, and finally set the current node to its right child
            else:
                curr = stack.pop()
                print(curr.data, end=' ')
                curr = curr.right
    def preorderIterative(self, root):
        if root is None:
            return
        # create an empty stack and push the root node
        stack = deque()
        stack.append(root)
        # loop till stack is empty
        while stack:
            curr = stack.pop()
            print(curr.data, end=' ')

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            
    def postorderIterative(self, root):
        if root is None:
            return 

        stack = deque()
        stack.append(root)
        # create another stack to store postorder traversal
        out = deque()
        while stack:
            # pop a node from the stack 
            # and push the data into the output stack
            curr = stack.pop()
            out.append(curr.data)
            # push the left and right child of the popped node 
            # into the stack
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            
        while out:
            print(out.pop(), end=' ')

    def inorderRecursive(self, root):
        if root is None:
            return
        self.inorderRecursive(root.left)
        print(root.data, end=' ')
        self.inorderRecursive(root.right)

if __name__ == '__main__':
    bt = BinaryTreeTraversal()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    bt.inorderIterative(root)   # 4 2 1 7 5 8 3 6 
    print()
    bt.inorderRecursive(root)   # 4 2 1 7 5 8 3 6 
    print()
    bt.preorderIterative(root)  # 1 2 4 3 5 7 8 6 
    print()
    bt.postorderIterative(root) # 4 2 7 8 5 6 3 1 