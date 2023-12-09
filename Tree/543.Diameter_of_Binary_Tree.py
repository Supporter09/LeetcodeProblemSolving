class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode()
root.val = 1
root.left = TreeNode(val=2)
root.right = TreeNode(val=3)
root.left.left = TreeNode(val=4)
root.left.right = TreeNode(val=5)
root.left.left.left = None
root.left.left.right = None
root.left.right.left = None
root.left.right.right = None

def diameterOfBinaryTree(root):
    res = [0]

    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0], 2 + left + right)

        return 1 + max(left, right)
    
    dfs(root)
    return res[0]

print(diameterOfBinaryTree(root))