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
    
    def printLL(self, node):
        if node is None:
            return None
        while node is not None:
            print (node.data)
            node = node.next

# Remove Negatives
# ------------------------------------------------------------------------------------
# Given a pointer to the head node of a singly linked list, remove any nodes containing negative values 
# and return the list.
    def removeNegatives(self, node):
        if node is None:
            return None
        prev = node
        temp = node.next
        while temp is not None:
            if temp.data < 0:
                prev.next = temp.next
                return
            else:
                prev = temp
                temp = temp.next
        return
# Partition
# ------------------------------------------------------------------------------------
# Create partition(ListNode, value) that locates the first node with that value, and moves all nodes with values 
# less than that value to be earlier, and all nodes with values greater than that value to be later.  
# Otherwise, original order need not be perfectly preserved. return the new head ListNode.
    def partition(self, node, value):
        prev = None
        temp = node
        while temp is not None:
            print("Im heree")
            if temp.data > value:
                prev = temp
                break
            temp = temp.next
        if prev:


linked_list = LinkedList() 

linked_list.addFront(5)
linked_list.addFront(4) 
linked_list.addFront(3) 
linked_list.addFront(-2)
linked_list.addFront(-1)

#remove value
linked_list.removeNegatives(linked_list.head)
print('New list: ', linked_list.display(linked_list.head))
