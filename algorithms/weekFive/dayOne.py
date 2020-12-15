# Stack 
# ------------------------------------------------
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class Stack: 
    def __init__(self): 
        self.head = None
    
    def printLL(self, node):
        if node is None:
            return None
        while node is not None:
            print (node.data)
            node = node.next

# Stack Push
# ------------------------------------------------
# Create push(val) that adds val to our stack.
    def push(self, val):
        new_node = Node(val) 
        if self.head is None:  
            self.head = new_node  
            return
        last = self.head 
        while (last.next):  
            last = last.next
        last.next=new_node
        return self

# Stack Top
# ------------------------------------------------
# Return (not remove) the stack’s top value.
    def top(self):
        if self.head is None:  
            return self
        last = self.head 
        while (last.next):  
            last = last.next
        return last.data

# Stack Is Empty
# ------------------------------------------------
# Return whether the stack is empty.
    def isEmpty(self):
        if self.head is None:  
            return True
        else: 
            return False

# Stack Pop
# ------------------------------------------------
# Create pop() to remove and return the top val.
    def pop(self):
        if self.head is None:  
            return self
        temp = self.head
        while(temp.next is not None):
            prev  = temp
            temp = temp.next
        prev.next = None
        return temp.data

# Stack Contains
# ------------------------------------------------
# Return whether given val is within the stack.
    def contains(self, val):
        current = self.head
        while current is not None: 
            if current.data == val: 
                return True 
            current = current.next
        return False 

# Stack Size
# ------------------------------------------------
# Return the number of stacked values.
    def size(self):
        temp = self.head
        count = 0
        while temp is not None: 
            count += 1
            temp = temp.next
        return count 

stack1 = Stack() 

stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)

print(stack1.printLL(stack1.head))
print("---------------------------")
print(stack1.top())
print("---------------------------")
print(stack1.isEmpty())
print("---------------------------")
print(stack1.pop())
print("---------------------------")
print(stack1.printLL(stack1.head))
print("---------------------------")
print(stack1.contains(4))
print(stack1.contains(10))
print("---------------------------")
print(stack1.size())
