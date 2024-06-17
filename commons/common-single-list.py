"""
single list: only one pointer to the next node
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next

        return str(nodes)


if __name__ == "__main__":
    # Example usage
    n1 = Node('1')
    n2 = Node('2')
    n3 = Node('40')
    lklist = LinkedList()
    lklist.head = n1

    n1.next = n2
    n2.next = n3

    print(lklist)
