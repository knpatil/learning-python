
from linked_list import LinkedList

my_ll = LinkedList()
print("size =", my_ll.size())
my_ll.display()

my_ll.add(10)
print("size =", my_ll.size())
my_ll.display()

my_ll.add(20)
my_ll.add(30)
my_ll.add(40)
print("size =", my_ll.size())
my_ll.display()

print("Is 30 present ? ", my_ll.search(30))

print("Is 50 present ? ", my_ll.search(50))

print("Before removing")
my_ll.display()

my_ll.remove(20)

print("After removing")
my_ll.display()

my_ll.remove(30)
my_ll.display()

my_ll.add(70)
my_ll.display()

my_ll.remove(40)
my_ll.display()
print("size=", my_ll.size())

