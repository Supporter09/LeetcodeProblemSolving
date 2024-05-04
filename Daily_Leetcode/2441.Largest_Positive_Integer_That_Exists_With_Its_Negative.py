def findMaxK(nums):
    nums_dict = dict()
    res = -1
    for i in range(len(nums)):
        if -1 * nums[i] not in nums_dict:
            nums_dict[nums[i]] = 1
        else:
            res = max(res, abs(nums[i]))

    return res


print(findMaxK([-9, -43, 24, -23, -16, -30, -38, -30]))
