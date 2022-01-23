import sys
from collections import deque


def solution(n, zone, max_rain):
    ans = 0

    def bfs(x, y, rain):
        rangeX = [0, 1, 0, -1]
        rangeY = [-1, 0, 1, 0]

        q = deque()
        q.append([x, y])
        visited[x][y] = True

        while q:
            now_x, now_y = q.popleft()
            for i in range(4):
                tmp_x = now_x + rangeX[i]
                tmp_y = now_y + rangeY[i]

                if 0 <= tmp_x < n and 0 <= tmp_y < n and visited[tmp_x][tmp_y] is False:
                    if zone[tmp_x][tmp_y] > rain:
                        q.append([tmp_x, tmp_y])
                        visited[tmp_x][tmp_y] = True

    for r in range(max_rain + 1):
        tmp_ans = 0
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if zone[i][j] > r and visited[i][j] is False:
                    bfs(i, j, r)
                    tmp_ans += 1
        ans = max(tmp_ans, ans)

    return ans


n = int(sys.stdin.readline())
zone = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

rain = 0
for row in zone:
    rain = max(rain, max(row))

print(solution(n, zone, rain))
