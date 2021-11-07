import sys
from collections import deque

n = int(sys.stdin.readline())

area = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

home = []

rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    count = 1
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            temp_x = now_x + rangeX[i]
            temp_y = now_y + rangeY[i]
            if 0 <= temp_x < n and 0 <= temp_y < n and visited[temp_x][temp_y] is False:
                if area[temp_x][temp_y] == 1:
                    visited[temp_x][temp_y] = True
                    q.append([temp_x, temp_y])
                    count += 1

    home.append(count)


for i in range(n):
    for j in range(n):
        if area[i][j] == 1 and visited[i][j] is False:
            bfs(i, j)

home.sort()
print(len(home))
for i in home:
    print(i)
