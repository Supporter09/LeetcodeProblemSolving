class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Floyd's Tortoise and Hare
# Time Complexity: O(n)
# Space Complexity: O(1)
def hasCycle(head):
    slow, fast = head, head

    # Fast pointer always moves faster => Check if fast reach null or not => If true => Not contain a cycle
    while fast and fast.next:
        # Shift slow by 1 and fast by 2
        slow = slow.next
        fast = fast.next.next

        # If those meet each other => There is a loop
        if slow == fast:
            return True

    return False


# Idea for O(n) TC and O(n) SC:
# Save every node in a hash set and if the node we stay already in hash set => There is a loop
