# WAP  to  merge two list without using extend function
# create a function pass 2 list and append every element of 2nd list to 1st lis=t and print
# l1=[9,8,2]
# l2=[3,6,4]
# def merge(l1,l2):
#     for i in l2:
#         l1.append(i)
#     return l1
# newlist1=merge(l1,l2)
# print ("Merged list",newlist1)

# stack = []
# def push( element ):
#     stack.append(element)
# def pop( element ):
#     x=stack.pop()
# push(1)
# push(3)
# pop(0)
# print(stack)

# reverse list using stack 
# stack=[]
# def push( element ):
#     stack.append(element)
#     print(element,"Appended")

# def pop():
#     if len(stack)>0:
#         x=stack.pop()
#         print(x, "Popped")
#         # return x
#     else:
#         print ("Empty")

# push(9)
# push(5)
# push(6)
# print(stack)
# pop()
# pop()
# print(stack)

# x = [9,5,6,4]
# for i in x:
#     push(i)
# print("Reverse")
# while len(stack)>0:
#     print(pop(),end=" ")

# stack=[]
# def push( element ):
#     stack.append(element)
#     # print(element,"Pushed")

# def pop():
#     if len(stack)>0:
#         x=stack.pop()
#         return x
#     else:
#         print ("Empty")

# n=13

# while n>0:
#     r=n%2
#     push(r)
#     n=n//2

# while len(stack)>0:
#     print(pop(),end=" ")

# Write a code for atm machine for solving following conditions
# choice 1 is for chechking balance
# choice 2 is for deposit specific amount
# choice 3 is for withdraw amount
# choice 4 to exit from system

# def check_balance(balance):
#     print(f"\nYour current balance is: ₹{balance}\n")
#     return balance

# def deposit(balance):
#     amount = float(input("Enter the amount to deposit: ₹"))
#     if amount > 0:
#         balance += amount
#         print(f"₹{amount} deposited successfully!")
#     else:
#         print("Invalid deposit amount!")
#     return balance

# def withdraw(balance):
#     amount = float(input("Enter the amount to withdraw: ₹"))
#     if amount > balance:
#         print("Insufficient balance!")
#     elif amount <= 0:
#         print("Invalid withdrawal amount!")
#     else:
#         balance -= amount
#         print(f"₹{amount} withdrawn successfully!")
#     return balance

# def atm():
#     balance = 500
#     while True:
#         print("\n====== ATM Menu ======")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")
        
#         choice = input("Enter your choice (1-4): ")

#         if choice == "1":
#             balance = check_balance(balance)
#         elif choice == "2":
#             balance = deposit(balance)
#         elif choice == "3":
#             balance = withdraw(balance)
#         elif choice == "4":
#             print("Thank you for using the ATM, visit again!. Goodbye!")
#             break
#         else:
#             print("Invalid choice! Please try again.")
# atm()



# stack = []
# expression = input("Enter a postfix expression: ")
# exp = expression.split(" ")
# for i in range(len(exp)):
#     x=exp[i]
#     if x.isnumeric():
#         stack.append(int(x))
#     else:
#         op2 = stack.pop()
#         op1 = stack.pop()
#         if x=='+':
#             res = op1 + op2
#         if x=='-':
#             res = op1 - op2
#         if x=='*':
#             res = op1 * op2
#         if x=='/':
#             res = op1 / op2
#         stack.append(res)
# print(stack.pop())

# def precedence(ch):
#     if ch == '^' or ch == '$':
#         return 3
#     if ch == '*' or ch == '/':
#         return 2
#     if ch == '+' or ch == '-':
#         return 1
#     else:
#         return 0
# stack = []
# post = []
# exp = input("Enter a infix expression: ")
# for ch in exp:
#     if ch.isalpha():
#         post.append(ch)
#     else:
#         if ch == '(':
#             stack.append(ch)
#         elif ch == ')':
#             while precedence(stack[-1])>precedence(ch):
#                 post.append(stack.pop())
#             stack.pop()
#         else:
#             while precedence(stack[-1])==   precedence(ch):
#                 stack.append(ch)
# while len(stack)>0:
#     post.append(stack.pop())
# print ("Postfix Expression is: ",end=" ")
# for i in post:
#     print(i,end=" ")


# def precedence(ch):
#     if ch=='$':
#         return 3
#     elif ch=='/' or ch=='*':
#         return 2
#     elif ch=='+' or ch=='-':
#         return 1
#     else:
#         return 0

# stack = []
# stack.append('(')
# post = []
# exp = input("Enter infix expression: ")
# exp+= ')'
# for ch in exp:
#     if ch.isalpha():
#         post.append(ch)
#     else:
#         if ch == '(':
#            stack.append(ch)
#         elif ch == ')':
#             while stack[-1] != '(':
#                 post.append( stack.pop() )
#             stack.pop()
#         else:
#             while precedence(ch) <= precedence(stack[-1]):
#                 post.append(  stack.pop()  )
#             else:
#                 stack.append(ch)
# for i in post:
#     print(i,end=" ")


# s=6
# Q=[None]*s
# print(Q)
# f=-1
# r=-1

# def insert(data):
#     global r,f
#     if r==(len(Q)-1):
#         print("Full")
#     else:
#         r+=1
#         Q[r]=data
#         if f==-1:
#             f+=1

# def delete():
#     global r,f
#     if f==-1 or f>r:
#         print("Empty")
#     else:
#         x=Q[f]
#         f+=1
#         print("Deleted",x)

# def display():
#     global r,f
#     if f==-1 or f>r:
#         print("Empty")
#     else:
#         for i in range(f,len(Q)):
#             print(Q[i],end=" ")

# insert('A')
# insert('B')
# insert('C')
# insert('D')
# insert('E')
# insert('F')
# print(Q)
# insert('G')
# print(Q)
# delete()
# delete()
# delete()
# delete()
# delete()
# delete()

# print(Q)
# display()


# s=6
# Q=[None]*s
# print(Q)
# f=-1
# r=-1

# def insert(data):
#     global r,f
#     if r==(len(Q)-1):
#         print("Full")
#     else:
#         r+=1
#         Q[r]=data
#         if f==-1:
#             f+=1

# def delete():
#     global r,f
#     if f==-1 or f>r:
#         print("Empty")
#     else:
#         x=Q[f]
#         f+=1
#         print("Deleted",x)

# def display():
#     global r,f
#     if f==-1 or f>r:
#         print("Empty")
#     else:
#         print("[",end="")
#         for i in range(f,len(Q)):
#             print(Q[i],end=",")
#         print("]")

# insert('A')
# insert('B')
# insert('C')
# insert('D')
# insert('E')
# insert('F')
# print(Q)
# insert('G')
# print(Q)
# delete()
# delete()
# delete()
# delete()
# delete()
# delete()
# print(Q)
# display()


# s = 6
# Q = [None] * s
# print(Q)
# f = -1
# r = -1

# def insert(data):
#     global r, f
#     if r == (len(Q) - 1):
#         print("Full")
#     else:
#         r += 1
#         Q[r] = data
#         if f == -1:
#             f = 0

# def delete():
#     global r, f
#     if f == -1 or f > r:
#         print("Empty")
#     else:
#         x = Q[f]
#         Q[f] = None 
#         f += 1
#         print("Deleted", x)

# def display():
#     print(Q)

# insert('A')
# insert('B')
# insert('C')
# insert('D')
# insert('E')
# insert('F')
# display() 
# insert('G') 
# display()  
# delete()  
# delete()   
# display()   
# delete()
# delete()
# display()


# s = 6
# CQ = [None] * s
# f = -1
# r = -1

# def insert(data):
#     global r, f
#     if f==(r+1)%len(CQ):
#         print("Full")
#     else:
#         r= (r + 1) % len(CQ)
#        CQ[r] = data
#         if f == -1:
#             f = 0

# def delete():
#     global r, f
#     if f == -1:
#         print("Empty")
#     else:
#         if f==r:
#             f=r=-1
#         x = CQ[f]
#         CQ[f] = None 
#         f += 1
#         print("Deleted", x)
# def display():
#     global r, f
#     if f==-1:
#         print("Empty")
#     while(True):
#         i=f
#         print(CQ[i],end=" ")
#         if f==r:
#             return
#         else:
#             f=(f+1)%len(CQ)
# insert('A')
# insert('B')
# insert('C')
# insert('D')
# insert('E')
# insert('F')
# print(CQ) 
# insert('G') 
# delete()  
# delete()   
# print(CQ)
# delete()
# delete()
# print(CQ)
# insert('H')
# insert('I')
# print(CQ)
# insert('J')
# print(CQ)
# # delete()
# delete()
# # print(CQ)
# display()

# Program: Decimal to Binary conversion using Stack

# def decimal_to_binary(n):
#     stack = []

#     while n > 0:
#         remainder = n % 2
#         stack.append(remainder)
#         n //= 2

#     binary = ""
#     while stack:
#         binary += str(stack.pop())
#     return binary if binary else "0"

# if __name__ == "__main__":
#     num = int(input("Enter a decimal number: "))
#     print("Binary representation:", decimal_to_binary(num))


# Simple program: Decimal to Binary using Stack

# n = int(input("Enter decimal number: "))
# stack = []

# while n > 0:
#     stack.append(n % 2)
#     n //= 2

# print("Binary representation: ", end="")
# while stack:
#     print(stack.pop(), end="")


# size = 5
# CQ = [None] * size
# f = -1
# r = -1
# def insert(data):
#     global r,f
#     if f == (r + 1) % size:
#         print("Full")
#     else:
#         r = (r + 1) % size
#         CQ[r] = data
#         print("Inserted:", data)
#         if f == -1:
#             f = 0
# def delete():
#     global r,f 
#     if f == -1:
#         print("Empty")
#     else:
#         x = CQ[f]
#         CQ[f] = None
#         if f == r:
#             f = r = -1
#         else:
#             f = (f + 1) % size 
#         print("Deleted:",x)
# def display():
#     global r,f 
#     if f == -1:
#         print("Empty")
#     else:
#         while(True):
#             i = f 
#             print(CQ[i], end = " ")
#             if f == r:
#                 return
#             else:
#                 f = (f + 1) % size    
# insert('A')
# insert('B')
# insert('c')
# insert('D')
# insert('E')
# insert('F')
# insert('G')
# print(CQ)
# delete()
# delete()
# delete()
# insert('T')
# display()



# def dfs_trav(graph, node, visited=None):   # Declares the function for traverse

#     if visited is None:     #It's starts with none and initial

#        visited set()

#     if node not in visited:  #node is not visited it will print

#        print(node, end="")

#        visited.add(node)   #mark it as visited

#        for neigh in graph[node]:  #call for its neigh

#            dfs_trav (graph, neigh, visited)

# graph = {

#         'A': ['B', 'C',]
#         'B': ['D', 'E'],
#         'C': ['F'],
#         'D': [],
#         'E': ['F'],
#         'F': []
#         }
# print("Depth First Traversal: ", end="")
# dfs_trav(graph, 'A')


# stack = []
# top = -1

# def push(element):
#     global top
    
#     stack.append(element)
#     top =top+1
#     print(element, "is pushed")

# def pop():
#     global top
#     if top == -1:
#         print("Stack is empty")
#     else:
#         x = stack.pop()
#         print(x, "is popped")
#         top -= 1

# def display():
#     global top
#     if top == -1:
#         print("Stack is empty")
#     else:
#         print("Stack elements:")
#         for i in range(top + 1):
#             print(stack[i], end=" ")
#         print()

# push(10)
# push(20)
# push(30)
# display()
# pop()
# display()

# def avg_numbers(a, b, c):
#     avg = (a + b + c) / 3
#     return avg


# a = float(input("Enter first number: ")) 
# b = float(input("Enter second number: ")) 
# c = float(input("Enter third number: ")) 
# average = avg_numbers(a,b,c) 
# print("The average is:", average)


# class Employee:
#     count = 0

#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         Employee.count += 1

#     def total_employees(cls):
#         return cls.count

#     def display(self):
#         print(f"Id: {self.id}, Name: {self.name}, Salary: {self.salary}")

# emp1 = Employee(101, "Ajay", 50000)
# emp2 = Employee(102, "Vijay", 60000)
# emp3 = Employee(103, "Sanjay", 70000)

# print("Total Employees:", Employee.total_employees())


# class employee:
#     counts=0

#     def __init__(self, id, name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         employee.counts += 1

#     def count(self):
#         print("Total Employees:",employee.counts)

#     def display(self):
#         print(f"Id: {self.id}, Name: {self.name}, Salary: {self.salary}")

# emp1 = employee(101, "Ajay", 50000)
# emp2 = employee(102, "Vijay", 60000)
# emp3 = employee(103, "Sanjay", 70000)

# emp1.count()

# employees = [emp1, emp2, emp3]

# for emp in employees:
#     emp.display()
