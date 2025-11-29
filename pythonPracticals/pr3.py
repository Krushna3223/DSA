# Program: Stack and its operations

stack = []
top = -1

def push(element):
    global top
    stack.append(element)
    top = top + 1
    print(element, "is pushed")

def pop():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        x = stack.pop()
        top = top - 1
        print(x, "is popped")

def display():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements:")
        for i in range(top + 1):
            print(stack[i], end=" ")
        print()

# Driver code
push(10)
push(20)
push(30)
display()
pop()
display()



