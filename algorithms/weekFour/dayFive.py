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

# Second Largest Value
# ------------------------------------------------------------------------------------
# Given a pointer to the first node in a singly linked list, return the second-largest value in the list.

    def secondLargestValue(self, node):
        if node is None:
            return None
        firMax = node
        secMax = node
        temp = node
        while temp is not None:
            if temp.data > firMax.data: 
                secMax = firMax
                firMax = temp
            elif (temp.data > secMax.data and temp.data != firMax.data): 
                secMax = temp.data  
            temp = temp.next

        return secMax.data
            

# Zip SLists
# ------------------------------------------------------------------------------------
# Provided two pointers to independent linked lists 'zip' the two lists together be alternating nodes.
# Start with the first list, and return the new list.

    def zipSLists(self, node1, node2):
        if node1 is None or node2 is None:
            return None
        pointer1 = node1
        pointer2 = node2
        temp = node1
        while temp is not None:
            temp.next = pointer2
            temp = pointer2.next
        temp = temp.next


linked_list = LinkedList() 

linked_list.addFront(5)
linked_list.addFront(4)
linked_list.addFront(3)
linked_list.addFront(-2)
linked_list.addFront(-1)

#second largest value
print('Second Larget Value:', linked_list.secondLargestValue(linked_list.head))

linked_list1 = LinkedList() 

linked_list1.addFront(5)
linked_list1.addFront(3)
linked_list1.addFront(1)

linked_list2 = LinkedList() 

linked_list2.addFront(6)
linked_list2.addFront(4)
linked_list2.addFront(2)

print(linked_list.printLL(linked_list1.head))
print(linked_list.printLL(linked_list2.head))

# zip lists
print('New List:', linked_list1.zipSLists(linked_list1.head, linked_list2.head))

