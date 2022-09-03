
class Node:
    def __init__(self, data):
        self.data = data
        self.left: "Node" = None
        self.right: "Node" = None

    def __repr__(self):
        return f"Node contains: {self.data}"


def are_symmetric(root1: Node, root2: Node):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.data != root2.data:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(
            root1.right, root2.left)


def is_symmetric(root):
  if root is None:
    return True
  return are_symmetric(root.right, root.left)

n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(4)
n5 = Node(4)
n6 = Node(6)

n1.left = n2
n1.right = n3
n2.right = n4
n3.left = n5

result = is_symmetric(n1)

print(f"Trees are symmetric: {result}")