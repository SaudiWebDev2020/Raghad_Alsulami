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

# length
# --------------------------------------------------------------------------------------------------
# Create a function that accepts a pointer to first list node, and returns number of nodes in sList.
    def length(self, node): 
        temp = node
        count = 0 
        while (temp): 
            count += 1
            temp = temp.next
        return count

# average
# --------------------------------------------------------------------------------------------------
# Create a standalone function average(node) that returns (…wait for it … ) the average of all values
# contained in that list.
    def average(self, length, node):
        count = length
        sum = 0
        while(node is not None):
            sum += node.data
            node = node.next
        return int (sum /count)

# min, max
# --------------------------------------------------------------------------------------------------
# Create function min(node) and max(node) to returning smallest and largest values in the list.
    def max(self, node):
        max = node.data
        while(node is not None):
            if node.data > max:
                max = node.data
            node = node.next
        return max
    
    def min(self, node):
        min = node.data
        while(node is not None):
            if node.data < min:
                min = node.data
            node = node.next
        return min

# display
# --------------------------------------------------------------------------------------------------
# Create display(node) for debugging that returns a string containing all list values. Build what you
# wish console.log(myList) did!
    def display(self, node):
        printval = node
        while printval is not None:
            print (printval.data)
            printval = printval.next


linked_list = LinkedList() 

linked_list.addFront(1)
linked_list.addFront(2) 
linked_list.addFront(3) 
linked_list.addFront(5)
node = linked_list.addFront(4)

#length
length = linked_list.length(node)
print('Length: ', length)
#avrage 
print('Avarage: ', linked_list.average(length, node))
#max 
print('Max: ', linked_list.max(node))
#min 
print('Min: ', linked_list.min(node))
#display
print ('Created linked list is:')
linked_list.display(node) 


