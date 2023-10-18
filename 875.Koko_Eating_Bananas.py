# Idea
# piles = [3,6,7,11], h = 8
# Possible k is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] (from 1 to max of piles)

# Use binary search
# l = 1
# r = max(piles)
# mid = l + (r - l) // 2

# Check if:
# KoKo can eat all piles with k = mid within h hours
# If True: check if there is any smaller k satisfy by r = mid - 1
# If False: check if there is larger k satisfy by l = mid + 1

def checkSatisfy(piles, h, k):
    time_take = 0
    for pile in piles:
        if pile % k == 0:
            time_take += pile // k
        else:
            time_take += pile // k + 1
    
    if time_take <= h:
        return True
    else:
        return False

def minEatingSpeed(piles, h):
    # Define two pointers
    l = 1
    r = max(piles)

    min_res = r

    while l <= r:
        mid = l + (r - l) // 2

        if checkSatisfy(piles, h, mid): # If current mid is a satisfied k => Check if any k smaller satisfy
            if mid < min_res:
                min_res = mid
            r = mid - 1
        else: # Current mid is not a satisfied k => Check larger k
            l = mid + 1

    return min_res

print(minEatingSpeed([3,6,7,11], 8)) 


