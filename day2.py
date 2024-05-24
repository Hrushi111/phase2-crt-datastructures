class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)                            
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Create a linked list
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
# Take input and add to the linked list
for i in range(4, 7):
    my_list.append(i)

# Display the linked list
my_list.display()

#length of linked list
def length(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count
def deletetailnode(head):
    curr=head
    if curr==None or curr.next==None:
        return None
    while curr.next.next!=none:
        curr=curr.next
        curr.next=None