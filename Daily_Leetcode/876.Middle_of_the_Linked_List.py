def middle_node(head):
    # 1. Khởi tạo 2 con trỏ slow và fast
    # sao cho fast di chuyển nhanh hơn slow 2 lần
    slow = head
    fast = head
    # 2. Khởi tạo biến index và prev để di chuyển slow
    index = 1
    prev = 0

    while fast is not None:
        # 3. Nếu hiệu của index / 2 và prev là 1 thì ta di chuyển slow lên 1 node
        if index // 2 - prev == 1:
            prev += 1
            slow = slow.next

        fast = fast.next
        index += 1
    # 4. Kết thúc vòng lặp ta trả về slow cũng là middle node của linked list
    return slow
