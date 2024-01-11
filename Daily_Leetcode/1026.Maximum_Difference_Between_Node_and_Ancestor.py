# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxVal = 0

        queue = deque([(root, root.val, root.val)])
        while queue:
            curr, high, low = queue.popleft()
            currVal = curr.val
            low_diff, high_diff = currVal - low, high - currVal
            maxVal = max(maxVal, low_diff, high_diff)

            if curr.left:
                queue.append((curr.left, max(currVal, high), min(currVal, low)))
            if curr.right:
                queue.append((curr.right, max(currVal, high), min(currVal, low)))

        return maxVal