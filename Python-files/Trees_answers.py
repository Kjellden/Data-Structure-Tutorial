""""
CSE 212 Lesson 9A Solved

Implementation of a basic Binary Search Tree data structure.
"""

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

        def __init__(self, name, job, wage):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.name = name
            self.job = job
            self.wage = wage
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, name, job, wage):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(name, job, wage)

        else:
            self._insert(name, job, wage, self.root)  # Start at the root

    def _insert(self,name, job, wage, node):
        """
        Write code that allows you to insert a new value to the tree (place by wage)
        """

        if wage < node.wage:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(name, job, wage)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(name, job, wage, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(name, job, wage)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(name, job, wage, node.right)
        
         
    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a loop
        is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        # write code the traverse forwards by the amount that people are payed
        """
        
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield (node.name, node.job, node.wage)
            yield from self._traverse_forward(node.right)

    def __reversed__(self):
        
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):
        """
        # write code the traverse backwards by the amount that people are payed
        """

        if node is not None:
            yield from self._traverse_backward(node.right) 
            yield (node.name, node.job, node.wage)
            yield from self._traverse_backward(node.left)


tree = BST()
tree.insert("kjellden", "coder", 15)
tree.insert("Nathan", "tester", 10)
tree.insert("Ryan", "management", 20)
tree.insert("John", "CEO", 25)


print("-----------------------")
print("test 1")
# test 1 print the list in reverse order by wage
for x in tree:
    print(x)  # ('Nathan', 'tester', 10) ('kjellden', 'coder', 15) ('Ryan', 'management', 20) ('John', 'CEO', 25)

print("-----------------------")
print("test 2")
# test 2 print the list in reverse order by wage
for x in reversed(tree):
    print(x) # ('John', 'CEO', 25) ('Ryan', 'management', 20) ('kjellden', 'coder', 15) ('Nathan', 'tester', 10)

