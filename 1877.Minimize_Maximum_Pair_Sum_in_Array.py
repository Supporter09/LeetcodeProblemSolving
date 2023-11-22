# The idea:
# When dealing with minimize pair sum => we need to distribute the weight of all number across all pairs. Therefore we 
# got minimize maximum pair
# Step 1: sort the array
# Step 2: take first and last element
def minPairSum(nums):
    nums = sorted(nums)
    l = 0
    r = len(nums) - 1
    min_max_pair = 0
    while l <= r:
        if nums[l] + nums[r] > min_max_pair:
            min_max_pair = nums[l] + nums[r]
        l += 1
        r -= 1
    return min_max_pair


print(minPairSum([4,1,5,1,2,5,1,5,5,4]))