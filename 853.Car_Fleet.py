# Idea
# Basically, each car fleet will have unique time to get to target
# Therefore, we can sort car by position and speed in reverse and check if time to get to target
# is greater than bottleneck or not. If yes, +1


def carFleet(target, position, speed):
    cars_right_to_left = sorted(zip(position, speed), reverse=True)

    bottleneck = float("-inf")
    fleets = 0
    print(cars_right_to_left)
    for d, s in cars_right_to_left:
        remaining_dist = target - d
        time_to_reach_target = remaining_dist / s

        if time_to_reach_target > bottleneck:
            bottleneck = time_to_reach_target
            fleets += 1

    return fleets


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
