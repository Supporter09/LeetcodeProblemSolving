# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive method
# For every node we visit => Switch left and right node
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      if not root:
        return None

      tmp = root.left
      root.left = root.right
      root.right = tmp

      self.invertTree(root.left)
      self.invertTree(root.right)

      return root