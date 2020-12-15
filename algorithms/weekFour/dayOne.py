# Node
#    - Constructor
#       -val
#       - next
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
# SinglyLinkList
#    -Constructor
#        - head
class LinkedList:
    def __init__(self):
        self.head = None

#    - addFront(val)
#        - add a new node to the beginning of the list
    def addFront(self, new_data):
        new_node = Node(new_data) 
        new_node.next=self.head
        self.head = new_node

#    - removeFront()
#       - removes and returns the first node of the list
    def removeFront(self):
        headval = self.head
        if headval is not None: 
            self.head = headval.next
            headval = None

#    - container(val)
#       - returns a boolean on whether or not the val is in the list
    def container(self, val):
        current = self.head
        while current != None: 
            if current.data == val: 
                return True # data found 
            current = current.next
        return False # Data Not found 

#    -  addBack(val)
#        - add new node to the end of the list
    def addBack(self, new_data):
        new_node = Node(new_data) 
        if self.head is None:  
            self.head = new_node  
            return
        last = self.head 
        while (last.next):  
            last = last.next
        last.next=new_node

#    - removeBack()
#       - removes and returns the last node of the list
    def removeBack(self):
        temp = self.head
        while(temp.next is not None):
            prev  = temp
            temp = temp.next
        prev.next = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next


if __name__=='__main__': 

    # start with the empty list 
    linked_list = LinkedList() 

    #add front 2, then then linked list becomes 2->None
    linked_list.addFront(2)
    print ('Created linked list is:')
    linked_list.listprint() 

    # add back 7, then linked list becomes 2-7->None
    linked_list.addBack(7)
    print ('Created linked list is:')
    linked_list.listprint() 

    #add front 3, then then linked list becomes 3-2-7->None
    linked_list.addFront(3)
    print ('Created linked list is:')
    linked_list.listprint() 

    #remove front, then then linked list becomes 2-7->None
    linked_list.removeFront()
    print ('Created linked list is:')
    linked_list.listprint() 

    #remove back, then then linked list becomes 2->None
    linked_list.removeBack()
    print ('Created linked list is:')
    linked_list.listprint() 

    # search for 4, should return false
    print(linked_list.container(4))

    # search for 2, should return true
    print(linked_list.container(2))