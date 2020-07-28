
from stack import Stack

my_stack = Stack()

my_stack.print()

print("Empty?", my_stack.isEmpty())
print("Size of the stack = ", my_stack.size())

my_stack.push(10)
my_stack.push(11)
my_stack.push(12)

my_stack.print()


print("Empty?", my_stack.isEmpty())
print("Size of the stack = ", my_stack.size())

item = my_stack.pop()
my_stack.print()

print("item popped = ", item)
print("Size of the stack = ", my_stack.size())

print("Top element = ", my_stack.peek())
my_stack.print()
