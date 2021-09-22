# 10026번 적록색약
import sys
from collections import deque

x = int(sys.stdin.readline())

map = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(x)]

rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]

visited = [[False] * x for _ in range(x)]


def dfs(row, col):
    if visited[row][col] is True:
        return 0
    q = deque()
    q.append([row, col])
    color = map[row][col]
    count = 0
    while q:
        now_y, now_x = q.popleft()
        print(now_y,now_x)
        for i in range(4):
            temp_y = now_y + rangeY[i]
            temp_x = now_x + rangeX[i]
            if 0 <= temp_x < x and 0 <= temp_y < x and visited[temp_y][temp_x] is False:
                if map[temp_y][temp_x] == color:
                    q.append([temp_y, temp_x])
                    visited[temp_y][temp_x] = True
                else:
                    count += 1
                    visited[temp_y][temp_x] = True
    return count

ans = 0
for i in range(x):
    for j in range(x):
        now =  dfs(i,j)
        print(now)
        ans += now
print(ans)
