import sys
from collections import deque


def bfs(x, y, n, sea):
    rangeX = [0, 1, 0, -1]
    rangeY = [-1, 0, 1, 0]

    q = deque()
    q.append([x, y, 0, 2])
    visited = [[-1] * n for i in range(n)]
    visited[x][y] = -2

    while q:
        feed = len(q)
        q = deque(sorted(q))

        now_x, now_y, count, size = q.popleft()

        for i in range(4):
            temp_x = now_x + rangeX[i]
            temp_y = now_y + rangeY[i]
            if 0 <= temp_x < n and 0 <= temp_y < n and visited[temp_x][temp_y] is -1:
                if sea[temp_x][temp_y] > size:
                    continue
                else:
                    if sea[temp_x][temp_y] == size:
                        size += 1
                    count += 1
                    visited[temp_x][temp_y] = min()
                    q.append([temp_x, temp_y, count, size])
    if min_time == 999999999:
        min_time = 0
    return min_time


def solution(n):
    sea = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                ans = bfs(i, j, n, sea)

    print(ans)


n = int(sys.stdin.readline())

solution(n)
