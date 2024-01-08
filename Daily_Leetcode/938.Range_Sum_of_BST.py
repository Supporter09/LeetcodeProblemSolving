# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def rangeSumBST( root, low, high) -> int:
    res = 0

    # BFS Method
    dq = deque([root])

    while dq:
        node = dq.pop()

        if low <= node.val <= high:
            res += node.val
        if node.left != None:
            dq.append(node.left)
        if node.right != None:
            dq.append(node.right)

    return res

node = TreeNode(val = 10)
node.left = TreeNode(val = 5)
node.right = TreeNode(val = 15)
node.left.left = TreeNode(val = 3)
node.left.right = TreeNode(val = 7)
node.right.left = TreeNode(val = 13)
node.right.right = TreeNode(val = 18)
node.right.right.left = None

print(rangeSumBST(node, 6, 10))