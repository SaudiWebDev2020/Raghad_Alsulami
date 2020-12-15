# Circular Queues
# ------------------------------------------------------------------------
# When Queue’s tail or head approaches ‘size’, wrap around to [0] and continue. 
# We cannot let tail and head meet – one can’t “lap” the other. Instead, 
# enqueue(val) should fail: Queue is full. Ditto dequeue() if Queue is empty. 
# Constructor requires a size argument. Starting there, let’s create a circular queue implementation!
class Node: 
    def __init__(self, data=None, next_node=None): 
        self.data = data 
        self.next = next_node 

class CirQueue():
    def __init__(self, cap):
        self.head = 0
        self.tail = 0
        self.capacity = cap
        self.data = [None]*cap

    def printQueue(self, node):
        if node is None:
            return None
        while node is not None:
            node = node.next

# Enqueue
# ------------------------------------------------------------------------
# Create enqueue(val) that adds val to our circular queue. Return false on fail. Wrap if needed!
    def enqueue(self, val):
        new_node = Node(val) 
        if self.head is None:  
            self.head = self.tail = new_node  
            return
        self.tail = new_node
        return self
# Front
# ------------------------------------------------------------------------
# Return (not remove) the queue’s front value.
    def front(self):
        if self.head is None:
            return None
        return self.head.data

# Is Empty
# ------------------------------------------------------------------------
# Return whether queue is empty.
    def isEmpty(self):
        if self.head is None:  
            return True
        else: 
            return False

# Is Full
# ------------------------------------------------------------------------
# Return whether queue is full.

# Dequeue
# ------------------------------------------------------------------------
# Create cirQueue method dequeue() that removes and returns the front value. Return null on fail.

# Contains
# ------------------------------------------------------------------------
# Return whether given val is within the queue.
    def contains(self, val):
        current = self.head
        while current is not None: 
            if current.data == val: 
                return True 
            current = current.next
        return False
        
# Size
# ------------------------------------------------------------------------
# Return number of queued vals (not capacity).
    def size(self):
        temp = self.head
        count = 0
        while temp is not None: 
            count += 1
            temp = temp.next
        return count 


queue1 = CirQueue(6) 
queue2 = CirQueue(0) 

queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(5)
queue1.enqueue(6)

print(queue1.printQueue(queue1.head))