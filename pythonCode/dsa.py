# def binary_search(my_list, low, high, x):
#   if low <= high:
#     mid = (low + high) // 2
#     if x == my_list[mid]:
#       return 1
#     elif x > my_list[mid]:
#       return binary_search(my_list, mid + 1, high, x)
#     else:
#       return binary_search(my_list, low, mid - 1, x)
#   else:
#     return -1

# my_list = [4,7,2,3,9,6]
# my_list.sort()
# print(my_list)
# x = int(input("Enter Value for search:"))
# low = 0
# high = len(my_list) - 1

# result = binary_search( my_list, low, high, x)
# if result == 1:
#   print("Found")
# else:
#   print("Not Found")



# class Node:
#     def __init__(self, info):
#         self.info = info
#         self.lc = None
#         self.rc = None


# class BinarySearchTree:
#     def __init__(self):
#         self.root = None


#     def insert(self,node,x):
#         if node == None:
#             newNode = Node(x)
#             newNode.info = x
#             newNode.lc = None
#             newNode.rc = None
#             return newNode
#         elif x<node.info:
#             node.lc=self.insert(node.lc,x)
#         else:
#             node.rc=self.insert(node.rc,x)
#         return node
    
#     def inorder(self, node):
#         if node is not None:
#             self.inorder(node.lc)
#             print(node.info, end=" ")
#             self.inorder(node.rc)


# b1 = BinarySearchTree()
# b1.root = b1.insert(b1.root, 8)
# b1.root = b1.insert(b1.root, 6)
# b1.root = b1.insert(b1.root, 4)
# b1.root = b1.insert(b1.root, 7)
# b1.root = b1.insert(b1.root, 10)
# b1.root = b1.insert(b1.root, 9)
# b1.inorder(b1.root)


# selection sort
# def selection_sort(A):
#     for i in range(len(A)):
#         min = A[i]
#         imin = i

#         for j in range(i+1, len(A)):
#             if A[j] < min:
#                 min = A[j]
#                 imin = j

#         temp = A[imin]
#         A[imin] = A[i]
#         A[i] = temp
#         print(A)
#     return A

# A = [55,44,22,67,11]
# print("Sorted list = ",selection_sort(A))

# radix sort
# def radix_sort(self,arr):
#     max_num = max(arr)
#     exp = 1                  

#     while max_num // exp > 0:
#         buckets = [[] for _ in range(10)]

#         for num in arr:
#             digit = (num // exp) % 10
#             buckets[digit].append(num)

#         arr = []
#         for b in buckets:
#             arr.extend(b)

#         exp *= 10

#     return arr

# arr = [170, 45, 75, 90, 802, 24, 2, 66]
# print(radix_sort(arr))



# class Node:
#     info = ""
#     lc = None
#     rc = None
# def insert(value,node):
#     if node == None:
#         nN = Node()
#         nN.info = value
#         nN.lc = None
#         nN.rc = None
#         return nN
#     elif value < node.info:
#         node.lc = insert(value,node.lc)
#     else:
#         node.rc = insert(value,node.rc)
#     return node

# def inorder(node):
#     if node != None:
#         inorder(node.lc)
#         print(node.info,'->', end=" ")
#         inorder(node.rc)

# def preorder(node):
#     if node != None:
#         print(node.info,'->', end=" ")
#         preorder(node.lc)
#         preorder(node.rc)

# def postorder(node):
#     if node != None:
#         postorder(node.lc)
#         postorder(node.rc)
#         print(node.info,'->', end=" ")

# root = None
# root = insert(45,root)
# root = insert(25,root)
# root = insert(55,root)
# root = insert(50,root)
# root = insert(35,root)
# root = insert(65,root)
# root = insert(15,root)
# print("inorder: ",end="")
# inorder(root)
# print("\npreorder: ",end="")
# preorder(root)
# print("\npostorder: ",end="")
# postorder(root)









# # structure of a node
# class Node:
#     def __init__(self,data=None):
#         self.info=data
#         self.next=None

# class SLL:
#     def __init__(self):
#         self.start=None

#     def insertNodeAtBeg(self,data):
#         #create a new node
#         self.newNode = Node()
#         self.newNode.info=data
#         self.newNode.next=None

#         if self.start==None:
#             self.start=self.newNode
#         # insert node at begining
#         else:
#             self.newNode.next=self.start
#             self.start=self.newNode
#         print(data,"Inserted at Beginning")
            
#     def insertNodeAtEnd(self,data):
#         #create a new node
#         self.newNode=Node()
#         self.newNode.info=data
#         self.newNode.next=None

#         if self.start==None:
#             self.start=self.newNode
#         # insert node at end
#         else:
#             self.p=self.start
#             while self.p.next!=None:
#                 self.p=self.p.next
#             self.p.next=self.newNode
#             print(data,"Inserted at End")
    
#     def insertNodeAtMiddle(self,data,pos):
#         #create a new node
#         self.newNode=Node()
#         self.newNode.info=data
#         self.newNode.next=None

#         if self.start==None:
#             self.start=self.newNode
#         # insert node at middle
#         else:
#             self.p=self.start
#             while self.p!=None and self.p.info!=pos:
#                     self.p=self.p.next
#                     if self.p==None:
#                         print("Position", pos, "not found!")
#                         return
#             self.q=self.p.next
#             self.p.next=self.newNode
#             self.newNode.next=self.q
#             print(data,"Inserted at Middle")

#     def DeleteNode(self,data):
#         if self.start==None:
#             print("Empty")
#         else:
#             self.p=self.start
#             while self.p.info!=data:
#                 if self.p.next==None:
#                     print("Not found")
#                     return
#                 self.q=self.p
#                 self.p=self.p.next
#             if self.start.info==data:
#                 self.start=self.start.next
#                 print(data,"Deleted from the Begining")
#                 return
#             elif self.p.next==None:
#                 self.q.next=None
#                 print(data,"Deleted from the End")

#             else:
#                 self.r=self.p.next
#                 self.q.next=self.r
#                 self.p.next=None
#                 print(data,"Deleted from the Middle")

#     def display(self):
#         if self.start==None:
#             print("Empty")
#         else:
#             p=self.start
#             while p is not None:
#                 print(p.info,end=" ")
#                 p=p.next
#             print()


# s1=SLL()
# s1.insertNodeAtBeg(10)
# s1.insertNodeAtBeg(20)
# s1.insertNodeAtBeg(30)
# s1.display()
# s1.insertNodeAtEnd(40)
# s1.insertNodeAtEnd(50)
# s1.display()
# s1.insertNodeAtMiddle(15,10)
# s1.display()
# s1.DeleteNode(30)
# s1.display()
# s1.DeleteNode(50)
# s1.display()
# s1.DeleteNode(10)
# s1.display()

# class node:
#     prev=None 
#     info=""
#     next=None
# class DLL:
#     def __init__(self):
#         self.start=None
#     def insertionAtBeg(self,data):
#         # CREATE A NEW NODE
#         nn=node() 
#         nn.prev=None
#         nn.info=data
#         nn.next=None  
        
#         if self.start==None:
#             self.start=nn
#         else:
#             nn.next=self.start
#             self.start.prev=nn
#             self.start=nn
#     def display(self):
#         if self.start==None:
#             print("empty")
#         else:
#             p=self.start
#             while p!=None:
#                 print(p.info)

#     def insertionAtEnd(self,data):
#         # CREATING A NEW NODE
#         nn=node()
#         nn.prev=None
#         nn.info=data
#         nn.next=None
#         if self.start==None:
#             self.start=nn
#         else:
#             p=self.start
#             while p.next!=None:
#                 p=p.next
#             p.next=nn
#             nn.prev=p             

#     def display(self):
#         if self.start==None:
#             print("empty")
#         else:
#             p=self.start
#             while p!=None:
#                 print(p.info)
#                 p=p.next 
#     def insertionAtMid(self,data,pos):
#                 # CREATING A NEW NODE
#         nn=node()
#         nn.info=data
#         nn.prev=None
#         nn.next=None
#         if self.start==None:
#             self.start=nn
#         else:
#             p=self.start
#             while p.info!=pos:
#                 q=p
#                 p=p.next
#             q.next=nn
#             nn.prev=q
#             nn.next=p
#             p.prev=nn
#     def display(self):
#         if self.start==None:
#             print("empty")
#         else:
#             p=self.start
#             while p!=None:
#                 print(p.info)
#                 p=p.next
#     def reverseNode(self):
#         if self.start==None :
#             print("empty")    
#         else:
#             p=self.start
#             while p.next!=None:
#                 p=p.next
#             while p!=None:
#                 print(p.info) 
#                 p=p.prev   
# n1=DLL()
# n1.insertionAtBeg(10)
# n1.insertionAtBeg(20)
# n1.insertionAtEnd(30)
# n1.insertionAtEnd(40)
# n1.insertionAtMid(50,30)
# print("before")
# n1.display()
# print("after")
# n1.reverseNode()








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










# class details:
#     def __init__(self,name,post,salary):
#         self.name=name
#         self.post=post
#         self.salary=salary
#     def display(self):
#         print(f"Name = {self.name}, Post = {self.post}, Salary = {self.salary}")

# d1=details("Ajay","Manager",2000)
# d2=details("Mahesh","Coder",1000)
# d3=details("Suresh","Debugger",500)
# d=[d1,d2,d3]
# for ch in d:
#     ch.display()

# stack=[]
# def push(data):
#     stack.append(data)
#     print(data," is pushed\n")
# def pop():
#     if len(stack)!=0:
#         x=stack.pop()
#         print(x,"is popped\n")
#     else:
#         print("Empty stack\n")
# def display():
#     print(stack)

# while True:
#     choice = int (input("Enter your choice: \n1. Push a element onto the stack\n2. Pop a element of the stack\n3. Display the stack\n4. Exit\n"))
#     if choice==1:
#         data=int(input("Enter the element to be pushed: "))
#         push(data)
#     elif choice==2:
#         pop()
#     elif choice == 3:
#         display()
#     elif choice ==4:
#         print("Exited successfully with no errors and return code 0")
#         break
#     else:
#         print("You have entered invalid choice enter correct choice")






# x=int(input("enter 1st no."))
# y=int(input("enter 2nd no."))
# print(x+y)










# # stack
# stack = []
# def push(data):
#     stack.append(data)
#     print("Pushed",data)
# def pop():
#     if len(stack)>0:
#         x=stack.pop()
#         print("Popped",x)
#         return x
# push(10)
# push(12)
# push(14)
# pop()
# print(stack)

# # Queue
# size = 4
# q=[None]*size
# f=-1
# r=-1
# def insert(data):
#     global r,f
#     if r==size-1:
#         print("Full")
#     else:
#         r+=1
#         q[r]=data
#         print("Inserted", data)
#         if f==-1:
#             f=0
# def delete():
#     global r,f
#     if f==-1 or f>r:
#         print("Empty")
#     else:
#         x=q[f]
#         f+=1
#         print("Deleted", x)
# def display():
#     global r,f
#     if f==-1 or f>r:
#         print("Empty")
#     else:
#         for i in range(f,size):
#             print(q[i])
# insert(11)
# insert(22)
# insert(33)
# insert(44)
# display()
# delete()
# delete()
# display()

# # Circular Queue
# size=4
# cq=[None]*size
# f=-1
# r=-1
# def insert(data):
#     global r,f
#     if f==(r+1)%size:
#         print("Full")
#     else:
#         r=(r+1)%size
#         cq[r]=data
#         print("Enqueued",data)
#         if f==-1:
#             f=0
# def delete():
#     global r,f
#     if f==-1:
#         print("Empty")
#     else:
#         x=cq[f]
#         if f==r:
#             f=r=-1
#         else:
#             f=(f+1)%size
#         print("Dequeued",x)
        
# def display():
#     global r,f
#     if f==-1:
#         print("Empty")
#     else:
#         i=f
#         while True:
#             print(cq[i])
#             if i==r:
#                 break
#             else:
#                 i = (i + 1) % size 
# insert(11)
# insert(22)
# insert(33)
# insert(44)
# display()
# delete()
# delete()
# display()



