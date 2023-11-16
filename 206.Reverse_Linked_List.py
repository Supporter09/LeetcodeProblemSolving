# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    arr = []
    while head:
        a = head.val
        res.insert(0, a)
        head = head.next
    print(arr)
    res = ListNode()
    for el in arr:
        res.val = el
        res.next = ListNode()

    
