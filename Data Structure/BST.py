# A binary search tree or BST is a binary tree that satisfies the following conditions:
#1. The left subtree of any node only contains nodes with keys less than the node's key
#2. The right subtree of any node only contains nodes with keys greater than the node's key

# Questions: Write a function to check if a binary tree is a binary search tree(BST)
# Write a function to find the maximum key in binary tree
# write a function to find the minimum key in a binary tree

def remove_None(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node =(is_bst_l and is_bst_r and max_l is None or node.key > max_l and max_r is None or node.key < max_r)

    min_key = min(remove_None([min_l, node.key, min_r]))
    max_kay = max(remove_None([max_l, node.key, max_r]))
    return is_bst_node, min_key, max_kay

# recursive implementation of insert

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return  node

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

# updating the value in BST:

def update(node, key, value):
    target = find(node, key)
    if target is not None:
       target.value = value

#list all node: write a function to retrieve all the key-values pairs stored in BST in the sorted order of keys

def list_all(node):
    if node is None:
        return []
    return list_all(node.left)+ [node.key, node.value] + list_all(node.right)

# the BST is a balanced tree

def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r  = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l- height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height