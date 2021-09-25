#7576번 토마토
import sys
from collections import deque


m, n = map(int, sys.stdin.readline().split())

box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#1은 익은 토마토,
# 정수 0은 익지 않은 토마토,
# 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
rangeX = [0, 1, 0, -1]
rangeY = [-1, 0, 1, 0]

q = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

if len(q) == i*j:
    print(0)
    sys.exit()

def bfs():
    while q:
        now_x, now_y = q.popleft();
        for i in range(4):
            temp_x = now_x + rangeX[i]
            temp_y = now_y + rangeY[i]
            if 0 <= temp_y < m and 0 <= temp_x < n:
                if box[temp_x][temp_y] == 0 :
                    box[temp_x][temp_y] = box[now_x][now_y] + 1
                    q.append([temp_x,temp_y])

bfs()
ans = 0
for i in box:
    for j in i :
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans,max(i))

print(ans-1)
