import sys

from itertools import permutations
n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))


ans = 0
kind = permutations(nums)
for per in kind:
    tmp = 0
    for i in range(n-1):
        tmp += abs(per[i] - per[i+1])

    ans = max(ans, tmp)

print(ans)