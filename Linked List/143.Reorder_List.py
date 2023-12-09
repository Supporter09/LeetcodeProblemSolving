# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Idea:
# Find the first half and second half by using Fast Slow Pointers:
# slow = head , fast = head.next
# slow + 1
# fast + 2
# When fast == null => slow.next is the start of the second half

# Reverse the second half
# Merge two half
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Implement fast slow pointer to find mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # Move 1 step
            fast = fast.next.next

        # Reverse the second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge two halfs
        first, second = head, prev
        while second: # Loop second half as length of second half is always smaller than length of first half
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next= tmp1
            first, second = tmp1, tmp2
