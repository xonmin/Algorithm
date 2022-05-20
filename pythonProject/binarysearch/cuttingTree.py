import sys

n, m = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))


def cutting(h):
    sum_left = 0
    for t in trees:
        if t - h < 0:
            continue
        sum_left += t - h
    return sum_left

max_tree = max(trees)
answer = 0
for i in range(max_tree):
    if cutting(i) >= m:
        answer = i
        break

print(answer)
