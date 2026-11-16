"""
Assignment-20: Binary Search Tree part-1

1. Define a class Node with instance variables left, item and right. The variables left
   and right are used to refer left and right child node. The item variable is used to hold
   data item.

2. Define a class BST to implement Binary Search Tree data structure. Make __init__()
   method to create root instance variable to hold the reference of root node.

3. In class BST, define insert method to store new data item in the binary search tree.

4. In class BST, define a search method to find a given item in the binary search tree
   and returns the node reference. It returns None if search failed.

5. In class BST, define a method to implement inorder traversal.

6. In class BST, define a method to implement preorder traversal.

7. In class BST, define a method to implement postorder traversal.

Solution approach ():-> 
                                      bst = BST()
                                      bst.insert(60)
                                           ↓
                                         data
                                          60
                                           ↓
root                                      self.root
 ↓                                           ↓
┌───────────────┐                    root = self.rinsert(root, data)
│ 2000 | 50 | 3000 │
└───────────────┘
       /       \
      ↓         ↓
┌────────┐   ┌────────┐
│ x | 30 | x │   │ x | 70 | x │
└────────┘   └────────┘
                  ↓
             ┌────────┐
             │ x | 60 | x │
             └────────┘

                    root.right = self.rinsert(3000, 60)
                    root = 3000, data = 60

                    root.left = self.rinsert(None, 60)


Assignment-21: Binary Search Tree Part-2

In class BST, define a method to find minimum value item node.
In class BST, define a method to find maximum value item node.
In class BST, define a method to delete a node from binary search tree.
In class BST, define a method size to return the number of elements present in the BST.

"""
class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left 
        self.right = right
class BST :
    def __init__(self):
        self.root = None
    def insert(self, data):
        self.root = self.rinsert(self.root, data)
    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root
    def search(self, data):
        return self.rsearch(self.root, data)
    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rsearch(root.left, data)
        else :
            return self.rsearch(root.right, data)
    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result
    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result
    def rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)
    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result
    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)
    def min_value(self,temp=None):
        current = temp or self.root
        while current.left is not None:
            current = current.left
        return current.item
    def max_value(self, temp = None):
        current = temp or self.root
        while current.right is not None:
            current = current.right
        return current.item
    def delete(self, data):
        self.root = self.rdelete(self.root, data)
    def rdelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            root.right=self.rdelete(root.right, root.item)
        return root
    def size(self):
        return len(self.inorder())

# ---------- Execution ----------
bst = BST()
for x in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(x)

print("Inorder  :", bst.inorder())     # [20, 30, 40, 50, 60, 70, 80]
print("Preorder :", bst.preorder())    # [50, 30, 20, 40, 70, 60, 80]
print("Postorder:", bst.postorder())   # [20, 40, 30, 60, 80, 70, 50]

print("Min:", bst.min_value())         # 20
print("Max:", bst.max_value())         # 80
print("Size:", bst.size())             # 7

found = bst.search(60)
print("Search 60:", found.item if found else None)   # 60
print("Search 99:", bst.search(99))                  # None

bst.delete(20)                         # leaf node
print("After deleting 20:", bst.inorder())   # [30, 40, 50, 60, 70, 80]

bst.delete(30)                         # one child
print("After deleting 30:", bst.inorder())   # [40, 50, 60, 70, 80]

bst.delete(50)                         # two children (root)
print("After deleting 50:", bst.inorder())   # [40, 60, 70, 80]
print("Preorder now:", bst.preorder())       # [60, 40, 70, 80]
print("Size:", bst.size())                   # 4