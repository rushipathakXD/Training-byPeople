# Binary Tree always has 2 or lesser children

# Types of Binary Tree -
#     Full Binary Tree -     It has either 2 child or 0 Child

#     Complete Binary Tree - All levels must be full except the last level
#                            The last level has all the nodes to extreme left as possible

#     Perfect Binary Tree -  All Leaf Node are at the same level
#                            All Non-leaf node must have 2 children

#     Balanced Binary Tree - Height difference between left and right subtree at any node
#                            must be max 1

#     Degenerate Binary Tree - Every node has one child

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
tea = Node("tea")
coffee = Node("coffee")
cola = Node("cola")
fanta = Node("fanta")

hot.left = tea
hot.right = coffee

cold.left = cola
cold.right = fanta

drinks.left = hot
drinks.right = cold

print(hot)
print(drinks.left)