"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if (self == None):
            self = BSTNode(value) # when would this be none?
            return
        else:
            if value < self.value:
                if self.left:
                    self.left.insert(value) # This is recursive- a recursive find. It has a base case of hitting end of tree. 
                    return
                else: 
                    self.left = BSTNode(value)
                    return
            if value >= self.value:
                if self.right: 
                    self.right.insert(value)
                    return
                else:
                    self.right = BSTNode(value)  ## Either calls insert (recursive) or init (constructor, new instance)
                    return
            
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif (target < self.value and self.left):
            return self.left.contains(target)
        elif (target >= self.value and self.right):
            return self.right.contains(target)
        else:
            return False
    

    # Return the maximum value found in the tree
    def get_max(self):
        cur_max = 0
        if (self):
            cur_max = self.value
        cur_node = self
        while (cur_node.right):
            cur_node = cur_node.right
            cur_max = cur_node.value
        return cur_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # depth first traversal with stack
        stack = []
        stack.append(self)
        while stack:
            p = stack.pop()
            fn(p.value)
            ### CALL FUNCTION HERE ###
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        # Left Root Right
        # depth traversal can be recursive or with a stack. This is the nature of trees
        if node:
            if node.left:
                node.left.in_order_print()
            print(node.value)
            if node.right:
                node.right.in_order_print()
        else:
            if self.left:
                self.left.in_order_print()
            print(self.value)
            if self.right:
                self.right.in_order_print()
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        if not self:
            return False
        queue = deque()
        queue.appendleft(self)
        while queue:
            p = queue.pop()
            print(p.value)
            if (p.left):
                queue.appendleft(p.left)
            if (p.right):
                queue.appendleft(p.right)    


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        stack = []
        if self:
            stack.append(self)
        while stack:
            p = stack.pop()
            print(p.value)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # Left leaf parent node right leaf up (hits root before right branch)
    # Root LeftNode-cascades RightNodes-cascade
    def pre_order_dft(self, node=None):
        if not self: 
            return False
        if self: 
            print(self.value) # start at root, or relative root
        if self.left:
            self.left.pre_order_dft() # the placemennt of recursive call creates a de facto stack
        if self.right:
            self.right.pre_order_dft()
        

    # Print Post-order recursive DFT
    # left leaf right leaf parent node of each - hits root last
    # LeftLeaf RightLeaf Parent 
    def post_order_dft(self, node=None):
        if not self:
            return False
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  