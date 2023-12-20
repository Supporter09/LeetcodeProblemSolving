# Idea:
# Recursive without duplicates element
# candidates = [2,3,6,7], target = 7
# we consider two branch
# first branch contain all combinations include at least one 2 [2]
# second branch contain all combinations that exclude 2 []

# Repeat this

def combinationSum(candidates, target):
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return
        
        cur.append(candidates[i])

        dfs(i, cur, total + candidates[i])

        cur.pop() # Not include this candidats
        dfs(i + 1, cur, total)

    dfs(0, [], 0)

    return res

print(combinationSum([2,3,6,7],7))