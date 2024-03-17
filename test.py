def combination(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1

    # Create a 2D array to store the computed values
    dp = [[0] * (r + 1) for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill the dp array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, min(i, r) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][r]

k, n = map(int, input().split())
print(combination(n, k) % (10**9 + 7)
