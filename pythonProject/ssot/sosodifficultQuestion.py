import math

def solution(levels):
    length = len(levels)
    sorted(levels)
    threshold = length * 0.75
    if isinstance(threshold, int):
        return levels[threshold + 1]
    else:
        return levels[math.ceil(threshold)]


print(solution([1, 2, 3, 4, 5, 6,7,8]))

