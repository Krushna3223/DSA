# Circular Linked List

class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class CLL:
    def __init__(self):
        self.start = None

    def insertAtBeg(self, data):
        nn = Node(data)
        if self.start is None:
            self.start = nn
            nn.next = nn
        else:
            p = self.start
            while p.next != self.start:
                p = p.next
            nn.next = self.start
            p.next = nn
            self.start = nn
        print(data, "Inserted at Beginning")

    def insertAtEnd(self, data):
        nn = Node(data)
        if self.start is None:
            self.start = nn
            nn.next = nn
        else:
            p = self.start
            while p.next != self.start:
                p = p.next
            p.next = nn
            nn.next = self.start
        print(data, "Inserted at End")

    def insertAtMid(self, data, pos):
        if self.start is None:
            print("List empty!")
            return
        
        nn = Node(data)
        p = self.start
        while p.info != pos:
            p = p.next
            if p == self.start:
                print("Position not found!")
                return
        
        nn.next = p.next
        p.next = nn
        print(data, "Inserted after", pos)

    def display(self):
        if self.start is None:
            print("Empty List")
            return
        
        p = self.start
        while True:
            print(p.info, end=" ")
            p = p.next
            if p == self.start:
                break
        print()

# Testing
c = CLL()
c.insertAtBeg(10)
c.insertAtEnd(20)
c.insertAtMid(15, 10)
c.insertAtEnd(30)
c.display()
