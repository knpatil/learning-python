
class Queue:
    def __init__(self):
        """
        initialize queue
        """
        self.items = []  # empty list

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0;

    def enqueue(self, item):       # O(n)
        #self.items.append(item) O(1)
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() # O(1)
        # if self.size() == 0:  # O(n)
        #     raise IndexError("queue is empty!")
        #
        # item = self.items[0]
        # del self.items[0] # removing
        # return item
