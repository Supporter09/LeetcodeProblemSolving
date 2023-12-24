class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)

    def update(self, node, start, end, idx, val):
        if start == end == idx:
            self.tree[node] += val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, left, right)
        right_sum = self.query(2 * node + 1, mid + 1, end, left, right)
        return left_sum + right_sum

def count_not_adjacent_subarrays(arr):
    n = len(arr)
    lis = [1] * n
    segment_tree = SegmentTree(n)

    # LIS Algorithm
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Update segment tree with LIS ending at each index
    for i in range(n - 1, -1, -1):
        segment_tree.update(1, 0, n - 1, i, 1)

    # Calculate count of strictly not adjacent subarrays using segment tree
    count = 0
    for i in range(n):
        segment_tree.update(1, 0, n - 1, i, -1)
        count += segment_tree.query(1, 0, n - 1, i + 1, n - 1)

    return count

# Example usage:
arr = [1,2,3,4]
result = count_not_adjacent_subarrays(arr)
print(result)
