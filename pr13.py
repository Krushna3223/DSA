# Stack using Linked List

class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        nn = Node(data)
        nn.next = self.top
        self.top = nn
        print(data, "Pushed")

    def pop(self):
        if self.top is None:
            print("Stack Empty")
        else:
            x = self.top.info
            self.top = self.top.next
            print(x, "Popped")

    def peek(self):
        if self.top is None:
            print("Stack Empty")
        else:
            print("Top element is:", self.top.info)

    def display(self):
        if self.top is None:
            print("Stack Empty")
        else:
            p = self.top
            print("Stack elements:", end=" ")
            while p is not None:
                print(p.info, end=" ")
                p = p.next
            print()


# Testing
s = StackLL()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()
s.peek()
