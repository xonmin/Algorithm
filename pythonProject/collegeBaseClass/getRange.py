import sys
from collections import deque


def solution(n, m, area):
    ans = []
    visited = [[False] * m for i in range(n)]
    count = 0
    def bfs(x, y):

        rangeX = [0, -1, 0, 1]
        rangeY = [1, 0, -1, 0]

        q = deque()
        q.append([x, y])
        visited[x][y] = True
        cnt = 1
        while q:
            now_x, now_y = q.popleft()
            for i in range(4):
                nx = now_x + rangeX[i]
                ny = now_y + rangeY[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] is False:
                    if area[nx][ny] == 0:
                        cnt += 1
                        q.append([nx, ny])
                        visited[nx][ny] = True
        return cnt

    for i in range(n):
        for j in range(m):
            if area[i][j] == 0 and visited[i][j] is False:
                ans.append(bfs(i, j))
                count += 1
    ans.sort()
    print(count)
    for i in ans:
        print(i, end=" ")


m, n, k = map(int, sys.stdin.readline().split())
black_base = []
area = [[0] * m for i in range(n)]

for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            area[i][j] = 1

solution(n, m, area)
