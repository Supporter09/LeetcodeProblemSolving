"""
- people[i] => weight of people i th
- each boat carry at most 2 people with limit weight
Idea:
- Sort the people by weight
- The ideal pair for a boat is the heaviest person with the lightest person
=> Use two pointers left right to match
"""


def numRescueBoats(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            boats += 1
        else:
            right -= 1  # The heaviest person cannot be paired with anyone else
            boats += 1

    return boats


print(numRescueBoats([1, 2], 3))
