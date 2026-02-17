class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

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

one.left = two
one.right = three

two.left = four
two.right = five

three.left = six
three.right = seven

def levelOrder(node):
    result = []
    queue = []
    queue.append(node)

    while len(queue)!=0:
        e = queue.pop(0)
        result.append(e.value)

        if(e.left is not None):
            queue.append(e.left)
        if(e.right is not None):
            queue.append(e.right)

    print(result)
    return result

print(levelOrder(one))