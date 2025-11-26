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


