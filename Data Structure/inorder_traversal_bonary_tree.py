# Traversal refers to the process of visiting each node of a tree exactly once. Visiting a node generally refers to
# adding the node's key to a list. There are three ways to traverse a binary tree and retur the list of visited keys

# Inorder traversal
#1. Traverse the left subtree recursively inorder
#2.Traverse the current node.
#3. Traverse the right subtree recursively inorder


#Preorder traversal
#1. Traverse the current node
#2. Traverse the left subtree recursively preorder
#3. Traverse the right subtree recursively preorder

#postorder traversal

# Implementation of inorder traversal:
def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left)+[node.key]+traverse_in_order(node.right))

#implementation of preorder traversal:

def traversal_in_pre_order(node):
    if node is None:
        return []
    return (
        node.key +
        traverse_in_order(node.left)+
        traverse_in_order(node.right)
    )

# write a function to calculate the height/depth of a binary tree
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# write a function to count the number of nodes in a binary tree
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


