import sys
from collections import deque


def bfs(x, y, size):
    rangeX = [0, 1, 0, -1]
    rangeY = [-1, 0, 1, 0]

    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append([x, y, 0])
    visited[x][y] = True
    feed = []

    while q:
        x, y, count = q.popleft()
        for i in range(4):
            nx = x + rangeX[i]
            ny = y + rangeY[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if sea[nx][ny] != 0 and sea[nx][ny] < size:
                    feed.append([nx, ny, count + 1])
                    q.append([nx, ny, count + 1])
                    visited[nx][ny] = True
                elif sea[nx][ny] == 0 or sea[nx][ny] == size:
                    visited[nx][ny] = True
                    q.append([nx, ny, count + 1])
    feed.sort(key=lambda x : (x[2],x[0],x[1]))
    if feed:
        return [feed[0][0], feed[0][1], feed[0][2]]
    else:
        return []


def solution(n):
    size = 2
    global sea
    sea = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    ans = 0
    feed = 0
    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 9:
                x, y = i, j
    while True:
        fish_eat = bfs(x, y, size)
        print(fish_eat)
        if fish_eat:
            new_x, new_y, count = fish_eat
            sea[new_x][new_y] = 0
            feed += 1
            ans += count
            if feed == size:
                size += 1
                feed = 0  # 먹은거 초기화
            x, y = new_x, new_y
        else:
            break
    print(ans)


n = int(sys.stdin.readline())

solution(n)
