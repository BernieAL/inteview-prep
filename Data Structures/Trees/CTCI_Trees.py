# """
# IMPLEMENTATION:
# https://high-python-ext-3-algorithms.readthedocs.io/ko/latest/chapter21.html#tree


# Ch#4 Trees and Graphs


# A tree is a type of graph
# A tree is a structure composed of nodes
# Each tree has a root node
# The root node has 0 or more child nodes
# each child node has 0 or mode child nodes and so on

# trees a structures made of nodes
# Trees cant have cycles

# Basic tree implementation can be done with just a Node class
# where the Node has 2 properties:
#     data and children

# class TreeNode(obj):
#     def __init__(self,data=None):
#         self.data = data
#         self.left = None
#         self.right = None


# BINARY TREE
# Each node has at MAX 2 children

# BINARY SEARCH TREE
# all left children are less than root
# and all right children are greater than root


# BALANCED VS UNBALANCED

# Balanced meaning not terribly unbalanced
# to ensure o(log n) insertion and search
# Balanced usually means the left and right branch differ
# by no MORE than 1 level 

# Types of balanced trees:
#     Red black and AVL

# COMPLETE BINARY TREE
#     every level of tree is filled except for the last level

# FULL BINARY TREE
#     every node has either zero or two children
#     no nodes have only one child

# PERFECT BINARY TREE
#     Tree that is FULL and COMPLETE
#     All lead nodes will be at the same level
#     and this level has the max num of nodes

# TRAVERSALS

#     INORDER
#         visit left branch
#         then root (current node)
#         then right branch
        
#         when performed on BST, nodes are visited in ascending order

#         def inorder(node):
#             if node != None:
#                 inorder(node.left)
#                 print(node.data)
#                 inorder(node.right)
        
#      PREORDER
#         visit root(current node) before children
#         visit left branch
#         visit right branch

#         root is always first node visited

#         def preorder(node):
#             if node != None:
#                 print(node.data)
#                 preoder(node.left)
#                 preorder(node.right)
        
#     POSTORDER
#         visit left branch
#         visit right branch
#         visit root(current node)

#         root is always last node visited

#         def postorder(node):
#             if node != None:
#                 postorder(node.left)
#                 postorder(node.right)
#                 print(node.data)


# BINARY HEAPS - MIN HEAPS AND MAX HEAPS

#     MIN HEAP:
        
#         A complete binary tree (completely filled other than rightmost elements on last level)
#         where each node is smaller than its children
#         The root is the minimum element in the tree

#         operations:
#             insert and extract_min
        
#         INSERT O(log n)
#             insertion into min-heap always starts at bottom
#             we insert at rightmost spot to maintain the complete tree property

#             then fix the tree by swapping the new element with its parent until we find the correct spot
#             for the inserted element. We 'bubble' up the minium element

#         EXTRACT MIN O(log n)
#             in min heap the min element is always at the top
#             to extract this:
#                 we have to remove the min element (root) and swap it with last element in heap
#                 (bottom-most and right-most) then bubble down this elelemnt, swapping with one of its children
#                 until min heap property is restored
#             Theres no inherent ordering betweeen left and right element
#             but we need to take the smaller on in order to maintain the min-heap order



# """


# class TreeNode():
#     def __init__(self,data=None,left=None,right=None):
#         self.data = data
#         self.left = left
#         self.right = right


# class BST():

            
#     def __init__(self,root=None):
#         self.root = root

#     def insert_Node(self,val):
#         newNode = TreeNode(val)
#         if self.root:
#             #will return true if able to insert, false if not able to insert
#             return self.insert_node_rec(self.root,val)
#         else:
#             #return true if inserted
#             self.root = newNode
#             return True
    
#     def insert_node_rec(self,root,val):
         
#          #this means the data is already there
#          #so we just return False
#          if root.data == val:
#              return False       
             
#          elif val < root.data:
#              #we check if left child exists already
#              #if it does, we recurse further down the left looking for empty spot
#              if root.left:
#                  return self.insert_node_rec(root.left,val)
#              else:
#                  #we found empty spot on left
#                  root.left = TreeNode(val)

        
#     def inorder(self):

#         if self.root != None:
#             self.inorder(self.root.left)
#             print(self.root.data)
#             self.inorder(self.root.right)

# t1 = BST(TreeNode(2))
# t1.insert_Node(1)
# t1.inorder()


