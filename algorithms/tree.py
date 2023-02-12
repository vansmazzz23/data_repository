class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)


def check_tree(tree_one, tree_two):
    if tree_one is None and tree_two is None:
        return True
    if tree_one is None or tree_two is None:
        return False
    return tree_one.val == tree_two.val and check_tree(tree_one.left, tree_two.left) and check_tree(tree_one.right, tree_two.right)


print(check_tree(tree, tree2))
