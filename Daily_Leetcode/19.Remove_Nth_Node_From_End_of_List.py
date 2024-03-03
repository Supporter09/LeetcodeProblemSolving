class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# TC: O(n), SC: O(1)


def removeNthFromEnd(head, n):
    # Kiểm tra edge case (head rỗng hoặc chỉ có 1 phần tử)
    if head is None or head.next is None:
        return None

    # Tạo 1 node giả để xử lý edge case
    # Xử lý edge case nếu phần tử đầu tiên bị xoá
    dummy = ListNode(0)
    dummy.next = head

    # Đếm số phần tử trong linked list và phần tử cần xoá sẽ là count - n
    count = 0

    iterater = head
    while iterater:
        count += 1
        iterater = iterater.next

    # Tìm phần tử cần xoá
    count -= n

    # Tìm phần tử trước phần tử cần xoá
    prev = dummy
    while count > 0:
        count -= 1
        prev = prev.next

    # Xoá phần tử thứ n từ cuối
    prev.next = prev.next.next

    return dummy.next
