def search(nums, target):
    # Define two pointer 
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2 # Use this to prevent overflow if the len(nums) is too big
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return False

def searchMatrix(matrix, target):
    # Define two pointer
    row_top = 0
    row_bot = len(matrix) - 1

    while row_top <= row_bot:
        mid = row_top + (row_bot - row_top) // 2
        
        # If target in current row
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            # Binary search target in current row
            res = search(matrix[mid], target)
            return res
        # If target > max value of current row
        elif target > matrix[mid][-1]: 
            row_top = mid + 1
        # If target < min value of current row
        elif target < matrix[mid][0]:
            row_bot = mid - 1

    return False

print(searchMatrix([
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]], 3))