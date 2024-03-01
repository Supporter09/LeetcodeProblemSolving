# Idea: Check how far we can go by bricks and ladders.
# The optimal way is to use ladders for the highest jumps and bricks for the rest.
# 1. Tracking the largest jumps r and remaing sum while iterating through the list.
# 2. Stop when the sum exceeds bricks.

import heapq


def furthestBuilding(heights, bricks, ladders):
    jumps = len(heights)
    heap = []
    for i in range(jumps - 1):
        d = heights[i + 1] - heights[i]
        if d > 0:
            heapq.heappush(heap, d)
            if len(heap) > ladders:
                print(heap)
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
    return jumps - 1


print(furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
