    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r-l)//2
        if nums[mid+1] < nums[mid]: # Find the min value
            return nums[mid+1]
        elif nums[mid] < nums[-1]: # The answer is on left half
            r = mid - 1
        elif nums[mid] >= nums[-1]: # The answer is on right half
            l = mid + 1