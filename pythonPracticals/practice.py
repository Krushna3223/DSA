
# arr = [45,7,9,8,0,6,7]
# f = int(input("ENTER NO TO FIND :"))
# a = 1
# for i in range(len(arr)):
#   if f == arr[i]:
#     a = 2
#     print("found at",i)
#     break
  
# if a==1:
#   print("nooooooo")



# def fact(n):
#   a = 1
#   for i in range(1,n+1):
#     a = a*i

#   print(a)  


# def fact(n):
#   if n == 0 or n == 1:
#     return 1
#   else:
#     return n * fact(n-1)


# n = int(input("e : "))
# print(fact(n))  

# size = int(input("Enter size of stack"))

# stack = [None]*size
# top = -1

# def push(data):
#   global top
#   if (top == size - 1):
#     print("aaaaaaaa")
#   else:
#     stack[top]=data
#     top = top+1  

  

# def pop():
#   global top
#   if top == -1:
#     print("nooooo")
#   else:
#     x = stack[top]
#     stack[top]=None
#     top = top -1  

# def show():
#   global top
#   if top == -1:
#     print("nooooo")
#   else:
#      print("Stack elements:", stack[:top+1])

# # Testing
# push(10)
# push(20)
# push(30)
# show()
# pop()
# show()
  

# s = input("enter expresion by space ")
# exp = s.split()
# stack = []
# for i in exp:
#   if i.isnumeric:
#     stack.append(int(i))
#   else:
#     op1 = stack.pop()
#     op2 = stack.pop()

#     if i == "+":
#       print(op2 + op1)


a = int(input("size : -"))

que = [None]*a  

front = -1 
rear = -1

def enq(x):
  global rear , front
  if rear == a-1:
    print("full")
  else:
      

def deq(x):
  global rear , front

def show():
  global rear , front 









