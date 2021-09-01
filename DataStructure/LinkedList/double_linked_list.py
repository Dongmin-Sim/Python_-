from _typeshed import Self


class Node:
    def __init__(self, data, p, n) -> None:
        self.data = data
        self.prev = p
        self.next = n


class DLL:
    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.count = 0

    def push(self, n):
        node = Node(n, None, None)
        if self.count == 0:
            self.start = node
            self.end = node

        else:
