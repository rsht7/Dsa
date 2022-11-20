Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# PART 1, 2 TO CONVERT A SORTED ARRAY INTO BST



# binary tree node
class Node:
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None

# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
	
	if not arr:
		return None

	# find middle index
	mid = (len(arr)) // 2
	
	# make the middle element the root
	root = Node(arr[mid])
	
	# left subtree of root has all
	# values 
	root.left = sortedArrayToBST(arr[:mid])
	
	# right subtree of root has all
	# values >arr[mid]
	root.right = sortedArrayToBST(arr[mid+1:])
	return root

# A utility function to print the preorder
# traversal of the BST
def preOrder(node):
	if not node:
		return
	
	print ( node.data)
	preOrder(node.left)
	preOrder(node.right)

# driver program to test above function
"""
Constructed balanced BST is
  4
/   \
2    6
/ \ / \
1 3 5 7
"""

arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(arr)
b=preOrder(root)
print("PreOrder Traversal of constructed BST",b)




#PART 3

#TO DELETE A NODE IN BST


class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to do
# inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)

# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty,
	# return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node


# Given a binary search tree
# and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):

	# Base Case
	if root is None:
		return root

	# Recursive calls for ancestors of
	# node to be deleted
	if key < root.key:
		root.left = deleteNode(root.left, key)
		return root

	elif(key > root.key):
		root.right = deleteNode(root.right, key)
		return root

	# We reach here when root is the node
	# to be deleted.
	
	# If root node is a leaf node
	
	if root.left is None and root.right is None:
		return None

	# If one of the children is empty

	if root.left is None:
		temp = root.right
		root = None
		return temp

	elif root.right is None:
		temp = root.left
		root = None
		return temp

	# If both children exist

	succParent = root

	# Find Successor

	succ = root.right

	while succ.left != None:
		succParent = succ
		succ = succ.left

	# Delete successor.Since successor
	# is always left child of its parent
	# we can safely make successor's right
	# right child as left of its parent.
	# If there is no succ, then assign
	# succ->right to succParent->right
	if succParent != root:
		succParent.left = succ.right
	else:
		succParent.right = succ.right

	# Copy Successor Data to root

	root.key = succ.key

	return root


# Driver code#we will see the above balanced tree
""" Let us create following BST
			4
		   / \
		  2   6
		/ \ / \
	   1 3 5   7 """

root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 5)
root = insert(root, 7)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 1)
print("Inorder traversal of the modified tree")
inorder(root)
SyntaxError: invalid syntax

# PART 1, 2 TO CONVERT A SORTED ARRAY INTO BST



# binary tree node
class Node:
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None

# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):

	if not arr:
		return None

	# find middle index
	mid = (len(arr)) // 2

	# make the middle element the root
	root = Node(arr[mid])

	# left subtree of root has all
	# values
	root.left = sortedArrayToBST(arr[:mid])

	# right subtree of root has all
	# values >arr[mid]
	root.right = sortedArrayToBST(arr[mid+1:])
	return root

# A utility function to print the preorder
# traversal of the BST
def preOrder(node):
	if not node:
		return

	print ( node.data)
	preOrder(node.left)
	preOrder(node.right)

# driver program to test above function
"""
Constructed balanced BST is
  4
/   \
2    6
/ \ / \
1 3 5 7
"""

arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(arr)
b=preOrder(root)
print("PreOrder Traversal of constructed BST",b)




#PART 3

#TO DELETE A NODE IN BST


class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to do
# inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)

# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty,
	# return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node


# Given a binary search tree
# and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):

	# Base Case
	if root is None:
		return root

	# Recursive calls for ancestors of
	# node to be deleted
	if key < root.key:
		root.left = deleteNode(root.left, key)
		return root

	elif(key > root.key):
		root.right = deleteNode(root.right, key)
		return root

	# We reach here when root is the node
	# to be deleted.

	# If root node is a leaf node

	if root.left is None and root.right is None:
		return None

	# If one of the children is empty

	if root.left is None:
		temp = root.right
		root = None
		return temp

	elif root.right is None:
		temp = root.left
		root = None
		return temp

	# If both children exist

	succParent = root

	# Find Successor

	succ = root.right

	while succ.left != None:
		succParent = succ
		succ = succ.left

	# Delete successor.Since successor
	# is always left child of its parent
	# we can safely make successor's right
	# right child as left of its parent.
	# If there is no succ, then assign
	# succ->right to succParent->right
	if succParent != root:
		succParent.left = succ.right
	else:
		succParent.right = succ.right

	# Copy Successor Data to root

	root.key = succ.key

	return root


# Driver code#we will see the above balanced tree
""" Let us create following BST
			4
		   / \
		  2   6
		/ \ / \
	   1 3 5   7 """

root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 5)
root = insert(root, 7)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 1)
print("Inorder traversal of the modified tree")
inorder(root)



# TO REMOVE AN ELEMENT FROM THE ARRAY


# This function removes an element x from arr[] and
# returns new size after removal.
# Returned size is n-1 when element is present.
# Otherwise 0 is returned to indicate failure.
def deleteElement(arr,n,x):

	# If x is last element, nothing to do
	if arr[n-1]==x:
		return n-1

	# Start from rightmost element and keep moving
# elements one position ahead.

	prev = arr[n-1]
	for i in range(n-2,1,-1):
		if arr[i]!=x:
			curr = arr[i]
			arr[i] = prev
			prev = curr

	# If element was not found
	if i<0:
		return 0

	# Else move the next element in place of x
	arr[i] = prev
	return n-1


# Driver code
arr = [1,2,3,4,5,6,7]
n = len(arr)
x = 6
n = deleteElement(arr,n,x)
print("Modified array is")
for i in range(n):
	print(arr[i],end=" ")




# PART 4 TO DETERMINE THE SPACE COMPLEXITIES
    
1. To delete an element fom an array 
 space complexity is O(1)
    
2. To delete a node from BST
   The space complexity of a binary search tree is O(n)
   in both the average and the worst cases.          