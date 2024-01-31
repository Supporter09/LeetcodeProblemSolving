# Idea
# Using stack
def largestRectangleArea(heights):
    max_value = -1
    stack = []  # hold [index, height]

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_value = max(max_value, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        max_value = max(max_value, h * (len(heights) - i))

    return max_value
