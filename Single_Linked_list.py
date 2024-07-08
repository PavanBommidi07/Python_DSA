class Node:
    def __init__(self,data = None, Next = None):
        self.data = data
        self.Next = Next

class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        node = Node(data)
        node.Next = self.head
        self.head = node
    
    def insert_at_middle(self,data,position):
        node = Node(data)
        if position == 0:
            node.head = self.Next
            self.head = node
        else:
            n = self.head
            count = 0
            while n is not None and count < position-1:
                n = n.Next
                count += 1
            
            node.Next = n.Next
            n.Next = node

    def insert_at_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.Next is not None:
                n = n.Next
            n.Next = node
        
    def display(self):
        if self.head is None:
            return None
        else:
            n = self.head
            while n is not None:
                print(n.data," ----> ",end="")
                n = n.Next
    
    def del_at_beginning(self):
        if self.head is not None:
            self.head = self.head.Next

    def del_end_node(self):
        if self.head is None:
            return None
        if self.head.Next == None:
            self.head = None
            return None
        current_node = self.head
        previous_node = None
        while current_node.Next is not None:
            previous_node = current_node
            current_node = current_node.Next
        previous_node.Next = None


LL = Linked_list()
LL.insert(10)
LL.insert(20)
LL.insert(30)
LL.insert(40)
LL.insert_at_end(50)
LL.display()

LL.del_at_beginning()
print("After deleting the first node:")
LL.display()

LL.del_end_node()
print("After deleting the last node:")
LL.display() 