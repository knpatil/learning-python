
from queue import Queue

q = Queue()  # create a q object

print("size =",q.size())

q.enqueue("Pune")

print("size =",q.size())
q.enqueue("Mumbai")
q.enqueue("Delhi")
q.enqueue("Bangalore")
q.enqueue("Nashik")
q.enqueue("Dhule")

print("size =",q.size())

print("processing ...", q.dequeue())
print("size =",q.size())
print("processing ...", q.dequeue())
print("size =",q.size())
print("processing ...", q.dequeue())
print("size =",q.size())
print("processing ...", q.dequeue())
print("size =",q.size())
print("processing ...", q.dequeue())
print("size =",q.size())
print("processing ...", q.dequeue())
print("size =",q.size())

# print("processing ...", q.dequeue())
# print("size =",q.size())
