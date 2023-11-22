# Sort the input array nums in ascending order.
# Initialize a variable left to 0 to represent the left boundary of the window, and initialize a variable maxFreq to 0 to store the maximum frequency.
# Iterate through the array with a variable right representing the right boundary of the window.
# Calculate the total number of operations needed to make all elements in the current window equal. This can be done by multiplying the difference between the current element and the previous element by the distance between the current and previous elements.
# If the total operations exceed k, move the left boundary of the window to the right.
# Update the maximum frequency based on the current window size.
# Continue this process until you reach the end of the array.

def maxFrequency(nums, k):
    nums = sorted(nums)

    maxFreq = 0

    # Initialize sliding window
    l = 0
    operations = 0
    for right in range(1, len(nums)):
        operations += (nums[right] - nums[right - 1]) * (right - l)

        if operations > k:
            operations -= nums[right] - nums[l]
            l += 1

        maxFreq = max(maxFreq, right - l + 1)

    return maxFreq

print(maxFrequency([1,4,8,13], 5))
    