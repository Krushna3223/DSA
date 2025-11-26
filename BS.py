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