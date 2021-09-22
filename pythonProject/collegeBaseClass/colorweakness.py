# 10026번 적록색약
import sys
from collections import deque

x = int(sys.stdin.readline())

map = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(x)]

rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]

visited = [[False] * x for _ in range(x)]
green_point = []


for i in range(x):
    for j in range(x):
        if map[i][j] == 'G':
            green_point.append([i, j])


def dfs(row, col):
    q = deque()
    q.append([row, col])
    color = map[row][col]
    while q:
        now_y, now_x = q.popleft()
        # print(now_y,now_x)
        for i in range(4):
            temp_y = now_y + rangeY[i]
            temp_x = now_x + rangeX[i]
            if 0 <= temp_x < x and 0 <= temp_y < x and visited[temp_y][temp_x] is False:
                if map[temp_y][temp_x] == color:
                    q.append([temp_y, temp_x])
                    visited[temp_y][temp_x] = True


def exe():

    ans = 0
    for i in range(x):
        for j in range(x):
            if visited[i][j] is False:
                dfs(i, j)
                ans += 1
            else:
                continue
    return ans


def colorweak():

    for gp in green_point:
        map[gp[0]][gp[1]] = 'R'
    rtn = exe()
    return rtn


normal = exe()
visited = [[False] * x for _ in range(x)]
weakness = colorweak()

print(normal,weakness)