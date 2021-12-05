import math
import sys


def solution(n, k, l):
    count = 0

    while k != l:
        k -= k // 2
        l -= l // 2
        count += 1
    return count


n, k, l = map(int, sys.stdin.readline().split())

print(solution(n, k, l))
