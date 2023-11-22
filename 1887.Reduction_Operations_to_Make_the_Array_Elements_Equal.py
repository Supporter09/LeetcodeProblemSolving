
def reductionOperations(nums):
    res = 0 # moves made so far

    nums.sort(reverse=True)

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]: # if the next number is strictly smaller... 
            # there are i + 1 numbers before
            # thus we need to apply the operation to all i + 1 numbers before
            res += i + 1
    print(res)
    return res

reductionOperations([7,9,10,8,6,4,1,5,2,3])

