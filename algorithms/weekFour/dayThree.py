class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

class LinkedList: 
    def __init__(self): 
        self.head = None
    
    def addFront(self, new_data):
        new_node = Node(new_data) 
        new_node.next=self.head
        self.head = new_node
        return new_node

# removeVal
# -----------------------------------------------------------------------------
# Create removeVal(list,value) that removes from our list the node with the given value. 
# Return the new list.
    def removeVal(self, node, val):
        if node is None:
            return None
        prev = node
        temp = node.next
        while temp is not None:
            if temp.data == val:
                prev.next = temp.next
                return val
            else:
                prev = temp
                temp = temp.next
        return

# prependVal
# -----------------------------------------------------------------------------
# Create prependVal(list,value,before) that inserts a listNode with given value immediately before 
# the node with before (or at end). Return the new list.
    def prependVal(self, node, val, before):
        newNode = Node(val)
        if node == None:
            return None
        while node.next is not None:
            if node.next.data == before:
                newNode.next = node.next
                node.next = newNode
                return
            else:
                node = node.next


# appendVal
# -----------------------------------------------------------------------------
# Create appendVal(list,value,after) that inserts a new listNode with given value immediately after 
# the node containing after (or at end). Return the new list.
    def appendVal(self, node, val, after):
        newNode = Node(val)
        if node == None:
            return None
        while node.next is not None:
            if node.next.data == after:
                newNode.next = node.next.next
                node.next.next = newNode
                return
            else:
                node = node.next

    def display(self, node):
        printval = node
        while printval is not None:
            print (printval.data)
            printval = printval.next

linked_list = LinkedList() 

linked_list.addFront(5)
linked_list.addFront(4) 
linked_list.addFront(3) 
linked_list.addFront(2)
linked_list.addFront(1)

#remove value
linked_list.removeVal(linked_list.head, 3)
print('New list: ', linked_list.display(linked_list.head))

linked_list.prependVal(linked_list.head, 7, 2)
print('New list: ', linked_list.display(linked_list.head))

linked_list.appendVal(linked_list.head, 10, 4)
print('New list: ', linked_list.display(linked_list.head))
