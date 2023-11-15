# Idea:
# Add 0 index to stack
# If index 1 > 0 => arr[stack.top()] = 1 - arr[stack.top()]
def dailyTemperatures(temperatures):
    # Initialize stack
    stack = []
    res = [0]*len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            tmpt , tmpi = stack.pop()
            res[tmpi] = i - tmpi
        stack.append([temp, i])
    print(res)
    return res

dailyTemperatures([73,74,75,71,69,72,76,73])

    