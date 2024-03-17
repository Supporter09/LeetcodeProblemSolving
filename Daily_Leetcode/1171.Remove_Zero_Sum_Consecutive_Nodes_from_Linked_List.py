# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# Idea:
# Use a prefix_sum to store the sum of the nodes from head to current node.
# If the prefix_sum appears again, it means the sum of the nodes between the two same prefix_sum is 0.
# So we can remove the nodes between them.
# Time Complexity: O(n)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = 0
    prefix_sums = {0: dummy}
