def findDuplicate(nums):
    # Find sum of all elements in the list and minus the sum of n natural numbers
    # to find the repeated number
    # Handle the case when only one integer appear 2 or more than 2 times
    n = len(nums) - 1
    count = 0
    check_num = nums[0]
    total = 0
    for num in nums:
        total += num
        if num == check_num:
            count += 1
        if count >= 2:
            return check_num

    return total - (n * (n + 1)) // 2


print(findDuplicate([3, 3, 3, 3, 3]))
