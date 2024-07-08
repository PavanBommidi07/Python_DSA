class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    def inorder(self):
        if self.right:
            self.left.inorder()
        
        print(str(self.value)+"--->",end="")

        if self.left:
            self.right.inorder()

root = Node(5)
root.left = Node(10)
root.right = Node(20)
root.inorder()