'''
Binary Search Tree is a binary tree(that is every node has two branches), 
in which the values contained in the left subtree is always less than the
root of that subtree, and the values contained in the right subtree is
always greater than the value of the root of the right subtree.
For more information about binary search trees, refer to :
http://en.wikipedia.org/wiki/Binary_search_tree
'''
#Only for use in Python 2.6.0a2 and later
from __future__ import print_function
class Node:

    # Constructor to initialize data
    # If data is not given by user,its taken as None 
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # __str__ returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s]" % (self.data,)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    '''
    While inserting values in a binary search tree, we first check
    whether the value is greater than, lesser than or equal to the
    root of the tree.
    We initialize current node as the root. 
    If the value is greater than the current node value, then we know that
    its right location will be in the right subtree. So we make the current
    element as the right node.
    
    If the value is lesser than the current node value, then we know that
    its right location will be in the left subtree. So we make the current
    element as the left node.

    If the value is equal to the current node value, then we know that the
    value is already contained in the tree and doesn't need to be reinserted.
    So we break from the loop.
    '''
    def insert(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            current = self.root

            while 1:
                if (current.data > val):
                    if (current.left == None):
                        current.left = Node(val)
                        break
                    else:
                        current = current.left

                elif (current.data < val):
                    if (current.right == None):
                        current.right = Node(val)
                        break
                    else:
                        current = current.right

                else:
                    break
    '''
    In preorder traversal, we first print the current element, then
    move on to the left subtree and finally to the right subree.
    '''
    def preorder(self, node):
        if (node == None):
            return
        else:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    '''
    In inorder traversal, we first move to the left subtree, then print
    the current element and finally move to the right subtree.
    '''
    
    #Important : Inorder traversal returns the elements in sorted form.
    def inorder(self, node):
        if (node == None):
            return
        else:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)
    '''
    In postorder traversal, we first move to the left subtree, then to the
    right subtree and finally print the current element.
    '''
    def postorder(self, node):
        if (node == None):
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
            
tree = BinarySearchTree()
tree.insert(1)
tree.insert(9)
tree.insert(4)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.insert(10)
tree.insert(0)
print ("Preorder Printing")
tree.preorder(tree.root)
print("\n\nInorder Printing")
tree.inorder(tree.root)
print("\n\nPostOrder Printing")
tree.postorder(tree.root)
