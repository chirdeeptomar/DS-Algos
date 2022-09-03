from pprint import pprint


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self.next:
            return f"Node contains: {self.data} and is connected to: {self.next.data}"

        return f"Node contains: {self.data} and is connected to: {self.next}"

    def connect(self, next):
        self.next = next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

pprint(n1)
pprint(n2)
pprint(n3)
pprint(n4)
pprint(n5)

n1.connect(n2)
n2.connect(n3)
n3.connect(n4)
n4.connect(n5)
n5.connect(n6)

pprint(n1)
pprint(n2)
pprint(n3)
pprint(n4)
pprint(n5)


def count_nodes(head: Node):
    count = 0

    current = head
    while current != None:
        count = count + 1
        current = current.next

    return count


total_nodes = count_nodes(n1)

pprint(f"Total Nodes: {total_nodes}")
