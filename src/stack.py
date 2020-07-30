#
# design stack data structure
#
# Operations
#
# push an item (add)
# pop an item (remove)
# peek (see what is at the top)
# isEmpty (check if stack if empty)
# size (how many elements are there inside a stack)
#
# NEW DATA TYPE/STRUCTURES ->
# int, float, str, char
#

# implement stack in python
# LIFO -- last in first out
# first in last out -- FILO
#

class Stack:

    def __init__(self):
        self.items = list()  # lists are dynamic,

    def is_empty(self):
        """check if the stack is empty or not"""
        if len(self.items) == 0:
            return True
        else:
            return False

    def peek(self):
        return self.items[len(self.items) - 1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print(self):
        print(self.items)
