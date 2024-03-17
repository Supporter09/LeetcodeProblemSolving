def getCommon(nums1, nums2):
    common = list(set(nums1) & set(nums2))

    if common:
        return min(common)
    else:
        return -1


print(getCommon([1, 2, 3, 6], [2, 3, 4, 5]))
