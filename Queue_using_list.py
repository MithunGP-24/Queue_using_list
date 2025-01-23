class Queue:
    def __init__(self):
        self.list = []
    def is_empty(self):
        return len(self.list) == 0

    def enqueue(self, data):
        return self.list.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            item = self.list.pop(0)  # Remove and return the first element
            return item
        else:
            return "Queue is empty"
    
    def get_rear(self):
        if not self.is_empty():
            return self.list[0]
    def get_front(self):
        if not self.is_empty():
            return self.list[-1]
        

    def display(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return len(self.list)

# Create an instance of Queue
o1 = Queue()
o1.enqueue(10)
o1.enqueue(20)
o1.enqueue(30)
o1.enqueue(40)
o1.enqueue(50)

print("Items are:", o1.display())
print("dequeue:", o1.dequeue())
print("rear element:", o1.get_rear())
print("front element:", o1.get_front())
print("Items are:", o1.display())


