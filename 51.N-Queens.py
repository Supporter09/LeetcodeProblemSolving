def solveNQueens(n):
    def backtrack(row, cols, diag1, diag2):
        if row == n:  # All queens are placed
            result.append(cols)  # Add position of queens in each row to result
            return
        for col in range(n):
            # Check if curr col is already occupied by other queen
            # Check if curr diag1 is already occupied by other queen
            # Check if curr diag2 is already occupied by other queen
            if col in cols or row - col in diag1 or row + col in diag2:
                continue
            backtrack(row + 1, cols + [col], diag1 + [row - col], diag2 + [row + col])

    result = []
    backtrack(0, [], [], [])
    return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


print(solveNQueens(4))
