# Queue - FIFO
# ------------------------------------------------
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class Queue: 
    def __init__(self): 
        self.head = None

    def printQueue(self, node):
        if node is None:
            return None
        while node is not None:
            print (node.data)
            node = node.next
# Front
# ------------------------------------------------
# Create slQueue method front() to return the value at front of our queue, without removing it.
    def front(self):
        if self.head is None:
            return None
        return self.head.data

# Is Empty
# ------------------------------------------------
# Create slQueue method isEmpty() that returns whether our queue contains no values.
    def isEmpty(self):
        if self.head is None:  
            return True
        else: 
            return False
# Enqueue
# ------------------------------------------------
# Create slQueue method enqueue(val) to add the given value to end of our queue. Remember, 
# slQueue uses a singly linked list (not an array). 
    def enqueue(self, val):
        new_node = Node(val) 
        if self.head is None:  
            self.head = new_node  
            return
        last = self.head 
        while (last.next):  
            last = last.next
        last.next=new_node
        return self
# Dequeue
# ------------------------------------------------
# Create slQueue method dequeue() to remove and return the value at front of queue. Remember, 
# slQueue uses a singly linked list (not array).
    def dequeue(self):
        headval = self.head
        if headval is not None: 
            self.head = headval.next
        return headval.data
# Contains
# ------------------------------------------------
# Create method contains(val) to return whether given value is found within our queue.
    def contains(self, val):
        current = self.head
        while current is not None: 
            if current.data == val: 
                return True 
            current = current.next
        return False 
# Size
# ------------------------------------------------
# Create slQueue method size() that returns the number of values in our queue.
    def size(self):
        temp = self.head
        count = 0
        while temp is not None: 
            count += 1
            temp = temp.next
        return count 

queue1 = Queue() 
queue2 = Queue() 

queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(5)
queue1.enqueue(6)

print(queue1.printQueue(queue1.head))
print("---------------------------")
print(queue1.front())
print("---------------------------")
print(queue1.isEmpty())
print(queue2.isEmpty())
print("---------------------------")
print(queue1.dequeue())
print("---------------------------")
print(queue1.printQueue(queue1.head))
print("---------------------------")
print(queue1.contains(4))
print(queue1.contains(10))
print("---------------------------")
print(queue1.size())