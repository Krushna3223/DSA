# Binary Search Tree Implementation

class Node:
    def __init__(self, info):
        self.info = info
        self.lc = None
        self.rc = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, x):
        if node is None:
            newNode = Node(x)
            return newNode
        elif x < node.info:
            node.lc = self.insert(node.lc, x)
        else:
            node.rc = self.insert(node.rc, x)
        return node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.lc)
            print(node.info, end=" ")
            self.inorder(node.rc)

    def preorder(self, node):
        if node is not None:
            print(node.info, end=" ")
            self.preorder(node.lc)
            self.preorder(node.rc)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.lc)
            self.postorder(node.rc)
            print(node.info, end=" ")

# Testing
b = BST()
b.root = b.insert(b.root, 50)
b.root = b.insert(b.root, 30)
b.root = b.insert(b.root, 20)
b.root = b.insert(b.root, 40)
b.root = b.insert(b.root, 70)
b.root = b.insert(b.root, 60)
b.root = b.insert(b.root, 80)

print("Inorder: ", end="")
b.inorder(b.root)

print("\nPreorder: ", end="")
b.preorder(b.root)

print("\nPostorder: ", end="")
b.postorder(b.root)
