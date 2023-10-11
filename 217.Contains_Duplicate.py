
def containsDuplicate(nums):
    count = {}
    for num in nums:
        if count.get(num) == None:
            count[num] = 1
        else:
            return True
    return False

print(containsDuplicate([1,2,3,1]))