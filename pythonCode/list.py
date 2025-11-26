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