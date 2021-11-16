# 1937 욕심쟁이 판다

import sys
from collections import deque
#파이썬 리컬전 depth 최대치 활성화해야 런타임 에러 안뜸
sys.setrecursionlimit(40000)
n = int(sys.stdin.readline())



forest = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]
visit = [[-1] * n for _ in range(n)]


def lookingForBamBoo(x, y):
    if visit[x][y] != -1:
        return visit[x][y]

    bamboo = forest[x][y]
    visit[x][y] = 1
    for i in range(4):
        temp_x = x + rangeX[i]
        temp_y = y + rangeY[i]
        if 0 <= temp_x < n and 0 <= temp_y < n and forest[temp_x][temp_y] > bamboo:

            visit[x][y] = max(1 + lookingForBamBoo(temp_x, temp_y), visit[x][y])

    return visit[x][y]



ans = 0
for i in range(n):
    for j in range(n):
        ans = max(lookingForBamBoo(i,j), ans)


print(ans)
