def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    path = set()  # Don't revisit the same location

    def dfs(r, c, i):
        if i == len(word):
            return True
        # Invalid conditions
        # Out of bounds
        # Not right character we need to find
        # Visit the same location
        if (
            r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or word[i] != board[r][c]
            or (r, c) in path
        ):
            return False

        path.add((r, c))
        # Go 4 directions
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )

        path.remove((r, c))  # Backtrack

        return res

    for r in range(ROWS):
        for c in range(ROWS):
            if dfs(r, c, 0):
                return True

    return False
