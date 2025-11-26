# Program: Queue and its operations

size = 6
Q = [None] * size
front = -1
rear = -1

def enqueue(data):
    global rear, front
    if rear == size - 1:
        print("Queue Full")
    else:
        rear += 1
        Q[rear] = data
        if front == -1:
            front = 0
        print("Inserted:", data)

def dequeue():
    global rear, front
    if front == -1 or front > rear:
        print("Queue Empty")
    else:
        x = Q[front]
        front += 1
        print("Deleted:", x)

def display():
    global rear, front
    if front == -1 or front > rear:
        print("Queue Empty")
    else:
        print("Queue elements:", end=" ")
        for i in range(front, rear + 1):
            print(Q[i], end=" ")
        print()

# Testing
enqueue('A')
enqueue('B')
enqueue('C')
display()
dequeue()
display()
