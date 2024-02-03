# 2966. Divide Array Into Arrays With Max Difference
def divideArray(nums, k):
    # n is a multiple of 3 => no need to check if n % 3 == 0
    nums.sort()
    res = []

    for i in range(0, len(nums), 3):
        # Because the array is sorted so the largest difference between elements
        # in array is nums[i+2] - nums[i]
        if i + 2 < len(nums) and nums[i + 2] - nums[i] <= k:
            res.append(nums[i : i + 3])
        else:
            return []
    return res


print(divideArray([1, 3, 3, 2, 7, 3], 3))
