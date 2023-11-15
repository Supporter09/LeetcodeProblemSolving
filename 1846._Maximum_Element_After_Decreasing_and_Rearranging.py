# The goal here is create a list that satisfied NOT count how many step 
# Therefore we can sort array and replace first element with 1 if necessary
# After that, replace a[i] = a[i-1] + 1 if a[i] - a[i-1] > 1
def maximumElementAfterDecrementingAndRearranging(arr):
    arr = sorted(arr)
    if arr[0] != 1:
        arr[0] = 1
    
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            arr[i] = arr[i-1] + 1
    # print(arr)
    # print(max(arr))
    return max(arr)

maximumElementAfterDecrementingAndRearranging([73,98,9])