# Queue using Linked List

class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        nn = Node(data)
        if self.front is None:
            self.front = nn
            self.rear = nn
        else:
            self.rear.next = nn
            self.rear = nn
        print(data, "Enqueued")

    def dequeue(self):
        if self.front is None:
            print("Queue Empty")
            return
        x = self.front.info
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(x, "Dequeued")

    def peek(self):
        if self.front is None:
            print("Queue Empty")
        else:
            print("Front element is:", self.front.info)

    def display(self):
        if self.front is None:
            print("Queue Empty")
            return

        p = self.front
        print("Queue elements:", end=" ")
        while p is not None:
            print(p.info, end=" ")
            p = p.next
        print()

# Testing
q = QueueLL()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
q.peek()
