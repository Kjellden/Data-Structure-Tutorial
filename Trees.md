# Python Data Structure Trees
## what is a Tree
A tree is like a linked list in that Node connects to another node but unlike linked lists tree nodes connect to multiple different nodes. the top node in a tree is called a root and each node is a parent and the nodes that connect to it are called a child lastly a node that does not have any child nodes are known as leaf nodes or end nodes.
![Tree](Images\tree-search.png)
## Binary search trees
A Binary search tree is a method of using trees. You use this type of tree buy saving a value in the nodes. When place or looking for a value you start at the root and move left or right depending on if the value is greater then or less the nodes value. 
![Tree](Images\bio-tree.png)
With this image we can see that if we are looking fro the number 6 we start at the root node (8) 8>6 so we move to the left now we look at the node (3) 6>3 so we move to the right 6=6 so this is the node that 6 is at.

## commands and Big O
Operation | Description | Performance
-------- | -------- | --------
insert(Value)| place a value in a new node | O(logn) 
remove(Value)|Remove a value from the tree.| O(log n) 
contains(Value)|Determine if a value is in the tree. |O(log n)
traverse_forward|Visit all objects from smallest to largest.|O(n)
traverse_reverse|Visit all objects from largest to smallest.|O(n
height(node)|Determine the height of a node. If the height of the tree is needed, the root node is provided.|O(n)
size()|Return the size of the BST.|O(1)
empty|Returns true if the root node is empty. This can also be done by checking the size for 0.|O(1)

## example code
This is what the set up for a BST looks like.
```python
class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

```
This is the code that shows up to traverse a BST without this code you could not properly use for loops for run though the search tree. Notice how BST Trees use recursion to get the values out of the tree.
```python
def __iter__(self):
	"""
    Perform a forward traversal (in order traversal) starting from 
    the root of the BST.  This is called a generator function.
    This function is called when a loop	is performed:

	for value in my_bst:
		print(value)

	"""
	yield from self._traverse_forward(self.root)  # Start at the root

def _traverse_forward(self, node):
	"""
	Does a forward traversal (in-order traversal) through the 
	BST.  If the node that we are given (which is the current
	subtree) exists, then we will keep traversing on the left
	side (thus getting the smaller numbers first), then we will 
	provide the data in the current node, and finally we will 
	traverse on the right side (thus getting the larger numbers last).

	The use of the 'yield' will allow this function to support loops
	like:

	for value in my_bst:
		print(value)

    The keyword 'yield' will return the value for the 'for' loop to
    use.  When the 'for' loop wants to get the next value, the code in
    this function will start back up where the last 'yield' returned a 
    value.  The keyword 'yield from' is used when our generator function
    needs to call another function for which a `yield` will be called.  
    In other words, the `yield` is delegated by the generator function
    to another function.

	This function is intended to be called the first time by 
	the __iter__ function.
	"""
	if node is not None:
		yield from self._traverse_forward(node.left)
		yield node.data
		yield from self._traverse_forward(node.right)
```
## Problem
[Trees.py](Python-files\Trees.py) The problems that we will be facing today is to making a BST for a job force there will be 3 parts to the node the name of the employee, job, and income. The tree should be organized by the income of the workers. The challenges you will face is placing new employees into the tree, Displaying the name job and income of the employees in order of how much they make. You will also need to find employees and see if they are in the tree or not. 

Check these answers if you need help [Trees_answers-project.py](Python-files\Trees_answers.py)
