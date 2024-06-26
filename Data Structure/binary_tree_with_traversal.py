class TreeNode():
    def __init__(self,key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        if self is None:
            return 0
        return 1+ max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return  1 + TreeNode.size(self.left)+ TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return [TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right)]

    def traverse_in_pre_order(self):
        if self is None:
            return []
        return [[self.key]+ TreeNode.traverse_in_order(self.left) +  TreeNode.traverse_in_order(self.right)]

    # def display_keys(self, space ='\t', level=0):
    #     if self is None:
    #         print(space*level + '~')
    #
    #     if self.left is None and self.right is None:
    #         print(space*level + str(self.key))
    #         return
    #     self.display_keys(self.right, space, level+1)
    #     print(space*level + str(self.key))
    #     display_keys(self.left, space, level+1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple)and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

def remove_None(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node =(is_bst_l and is_bst_r
                  and max_l is None or node.key > max_l
                  and min_r is None or node.key < min_r)

    min_key = min(remove_None([min_l, node.key, min_r]))
    max_kay = max(remove_None([max_l, node.key, max_r]))
    return is_bst_node, min_key, max_kay

tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6,7,8)))

tree = TreeNode.parse_tuple(tree_tuple)
print(tree)
print(is_bst(tree))
print(tree.height())
print(tree.size())
print(tree.traverse_in_order())
print(tree.traverse_in_pre_order())
print(tree.to_tuple())