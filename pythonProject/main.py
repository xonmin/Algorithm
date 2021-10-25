import sys
from collections import deque

N , K =  map(int, sys.stdin.readline().split())


def findBrother(N, K):
    q = deque()
    q.append(N)
    chk = 0
    for
d