def prefixSum2D(a):
    C, R = len(a[0]), len(a)
    psa = [[0 for x in range(C)] for y in range(R)]
    psa[0][0] = a[0][0]

    # Filling first row
    # and first column
    for i in range(1, C):
        psa[0][i] = psa[0][i - 1] + a[0][i]
    for i in range(0, R):
        psa[i][0] = psa[i - 1][0] + a[i][0]

    # updating the values in
    # the cells as per the
    # general formula
    for i in range(1, R):
        for j in range(1, C):
            # values in the cells of
            # new array are updated
            psa[i][j] = psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + a[i][j]
    return psa


def countSubmatrices(grid, k):
    # Process prefix sum
    n, m = len(grid), len(grid[0])
    prefix = prefixSum2D(grid)

    for row in prefix:
        print(*row)
    # Count submatrices
    # For each submatrix, we can calculate the sum of the submatrix in O(1) time
    count = 0
    if grid[0][0] <= k:
        count += 1
    for i in range(1, n):
        if prefix[i][0] <= k:
            print("r: ", i)
            count += 1

    for j in range(1, m):
        if prefix[0][j] <= k:
            print("c: ", j)
            count += 1

    for i in range(1, n):
        for j in range(1, m):
            if prefix[i][j] <= k:
                print("coordinate: ", i, j)
                count += 1
    print(count)
    return count


countSubmatrices([[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20)
