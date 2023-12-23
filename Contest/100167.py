def count_increasing_subarrays(nums):
    n = len(nums)
    count = 0

    for i in range(n):
        j = i + 1
        while j < n and nums[j] > nums[j - 1]:
            j += 1
            count += 1

    return count

# Example usage:
nums = [6,5,7,8]
result = count_increasing_subarrays(nums)
print(result)
