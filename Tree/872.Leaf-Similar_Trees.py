# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea: DPS to last node and append to leaves array. 
# Do this for both tree and compare the results
def take_leaves(root):
    res = []

    def dfs(node):
        if not node.left and not node.right:
            res.append(node.val)
            return 0

        # Go left
        if node.left:
            dfs(node.left)
        # Go right
        if node.right:
            dfs(node.right)

    dfs(root)
    return res

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left_leaves = []
        right_leaves = []

        left_leaves = take_leaves(root1)
        right_leaves = take_leaves(root2)
        
        return left_leaves == right_leaves
        