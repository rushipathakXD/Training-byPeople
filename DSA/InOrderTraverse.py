class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)

five.left = three
five.right = four

three.left = two
three.right = nine

four.left = eight
four.right = ten

eight.left = one
eight.right = six

def inorder(node):
    if(node == None):
        return
    
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

inorder(five)