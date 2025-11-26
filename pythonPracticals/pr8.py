# Doubly Linked List Program

class Node:
    def __init__(self, data):
        self.info = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.start = None

    def insertAtBeg(self, data):
        nn = Node(data)
        if self.start is None:
            self.start = nn
        else:
            nn.next = self.start
            self.start.prev = nn
            self.start = nn
        print(data, "Inserted at Beginning")

    def insertAtEnd(self, data):
        nn = Node(data)
        if self.start is None:
            self.start = nn
        else:
            p = self.start
            while p.next is not None:
                p = p.next
            p.next = nn
            nn.prev = p
        print(data, "Inserted at End")

    def insertAtMid(self, data, pos):
        nn = Node(data)
        p = self.start
        while p is not None and p.info != pos:
            p = p.next

        if p is None:
            print("Position not found!")
            return

        nn.next = p.next
        nn.prev = p

        if p.next is not None:
            p.next.prev = nn

        p.next = nn
        print(data, "Inserted after", pos)

    def display(self):
        p = self.start
        while p is not None:
            print(p.info, end=" ")
            p = p.next
        print()

# Testing
d = DLL()
d.insertAtBeg(10)
d.insertAtEnd(20)
d.insertAtMid(15, 10)
d.display()
